FireGuardLLM: Intelligent Firewall Log Analysis with Local Large Language Models

FireGuardLLM is an innovative cybersecurity tool that leverages the power of local Large Language Models (LLMs) to analyze firewall logs and predict potential network attacks. This project combines traditional data preprocessing techniques with cutting-edge AI to enhance network security.

Key Features:
Utilizes local LLM deployment (via Ollama) for privacy-preserving analysis
Processes historical firewall logs to extract relevant features
Employs natural language prompts to query the LLM for attack prediction
Provides real-time threat assessment on incoming network traffic
Offers easy integration with existing firewall systems

FireGuardLLM aims to augment traditional rule-based firewall systems with AI-driven insights, helping security professionals identify and respond to potential threats more effectively. By using local LLMs, it maintains data privacy and reduces reliance on cloud-based services.

This project serves as a proof-of-concept for applying large language models to cybersecurity tasks, opening up new possibilities for intelligent, adaptive network protection. It's designed for medium-level Python developers and cybersecurity enthusiasts looking to explore the intersection of AI and network security.


1. Make sure you have Ollama installed and running on your local machine.
2. Install required Python packages: `pandas`, `numpy`, `scikit-learn`, and `requests`.
3. Prepare a CSV file named 'firewall_logs.csv' with your firewall log data. It should include columns for timestamp, source_ip, source_port, dest_port, protocol, and is_attack (1 for attack, 0 for normal traffic).
4. Place the 'firewall_logs.csv' file in the same directory as your Python script.
5. Run the Python script. It will load the data, preprocess it, use the local LLM (via Ollama) to make predictions, and then evaluate the results.

A few additional notes:

- This approach uses the LLM for each individual prediction, which can be slow for large datasets. For a real-world application, you might want to batch the predictions or use a different approach for larger scale data.
- The accuracy of this method heavily depends on the quality and relevance of the LLM you're using. Make sure you're using a model that has some understanding of network security concepts.
- This example uses a simple prompt. You might want to experiment with different prompt structures to improve the accuracy of the predictions.
- Remember that this is a proof of concept. In a real-world scenario, you'd want to implement additional error handling, logging, and possibly a more sophisticated way of interpreting the LLM's responses.
