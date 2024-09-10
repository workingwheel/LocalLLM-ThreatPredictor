FireGuard: Smart Firewall Log Analysis Using Local AI

Hey there! Let me tell you about FireGuard, this cool project I've been working on. It's all about using AI to make sense of those endless firewall logs and spot potential attacks before they become a real headache.

So, what's the big deal? Well, we're using these fancy AI models called Large Language Models (LLMs) right on your own machine. No need to send your sensitive data to the cloud – privacy first, right?

Here's what FireGuard can do:
- Crunch through your old firewall logs to find patterns
- Use AI to predict if something fishy is going on
- Give you a heads-up about threats in real-time - *feature coming soon.
- Play nice with your existing firewall setup

The cool part is how it combines old-school data crunching with cutting-edge AI. It's like teaching an old dog new tricks, but for your firewall!

I built this because I was tired of staring at endless logs, trying to spot the needle in the haystack. With FireGuard, it's like having a super-smart assistant who never sleeps.

If you're into Python and curious about how AI can beef up cybersecurity, this project is right up your alley. It's not perfect – more of a "let's see what's possible" kind of thing – but it's a start!

Want to give it a spin? Here's what you need to do:

Windows Steps:
1. Get Ollama up and running on your machine.
   https://ollama.com/library
    a. After installing, make sure you are running ollama as a service. you can do so by running "ollama serve" on your terminal.
    b. Open CMD and run the following command: set OLLAMA_HOST=0.0.0.0 #This step is optional ofc. This is only if you want to scale functionality. It basically tells Ollama service to listen on all network interfaces of the machine, making it accessible from other computers on the network, not just locally.
2. Install required Python packages (pandas, numpy, scikit-learn, and requests). #see required.txt

Linux Steps: On the way.


A. Grab your firewall logs and save them as 'firewall_logs.csv'. Make sure it has all the important stuff like timestamps, IPs, ports, and whether it was an attack or not. This is different with manufacturers. 
B. Put that CSV file in the same folder as the script. 
C. Run it and watch the magic happen! Not actual magic. It is your machine hammering that GPU of yours doing calculations. 1 + 1 = 2 and so on. Basic stuff. Just kidding.

Just a heads up – it might be a bit slow if you throw a ton of data at it. And yeah, the results are only as good as the AI model + the GPU you're using. It has been tested with gemma2:27b and nidia 4090. Play around with different ways of asking the AI about the logs; you might stumble onto something that works even better!

*Tested with Asus, and Fortinet firewall applicances. Good luck.

Happy hunting, and may your networks stay secure!
