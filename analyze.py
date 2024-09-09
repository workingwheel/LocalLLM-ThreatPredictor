import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import requests
import json

# Load and preprocess data
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    data['day_of_week'] = data['timestamp'].dt.dayofweek
    return data

# Feature engineering
def engineer_features(df):
    df['connections_last_hour'] = df.groupby('source_ip')['timestamp'].transform(
        lambda x: x.rolling('1H').count()
    )
    df = pd.get_dummies(df, columns=['protocol'], prefix='proto')
    return df

# Prepare data for LLM
def prepare_data_for_llm(df):
    features = ['hour', 'day_of_week', 'source_port', 'dest_port', 
                'connections_last_hour', 'proto_TCP', 'proto_UDP']
    X = df[features]
    y = df['is_attack']
    return X, y

# Function to query Ollama
def query_ollama(prompt, model="llama2"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()['response']

# Predict using LLM
def predict_with_llm(X):
    predictions = []
    for _, row in X.iterrows():
        prompt = f"Based on the following firewall log entry, determine if this is likely an attack or normal traffic. Respond with only 'attack' or 'normal'.\n\nHour: {row['hour']}\nDay of week: {row['day_of_week']}\nSource port: {row['source_port']}\nDestination port: {row['dest_port']}\nConnections in last hour: {row['connections_last_hour']}\nTCP: {row['proto_TCP']}\nUDP: {row['proto_UDP']}"
        response = query_ollama(prompt)
        predictions.append(1 if 'attack' in response.lower() else 0)
    return predictions

# Main process
if __name__ == "__main__":
    # Load and preprocess data
    data = load_and_preprocess_data('firewall_logs.csv')
    data = engineer_features(data)
    X, y = prepare_data_for_llm(data)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Make predictions using LLM
    print("Making predictions...")
    y_pred = predict_with_llm(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
