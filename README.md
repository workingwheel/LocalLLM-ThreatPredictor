FireGuardLLM: Smart Firewall Log Analysis Using Local AI

Hey there! Let me tell you about FireGuardLLM, this cool project I've been working on. It's all about using AI to make sense of those endless firewall logs and spot potential attacks before they become a real headache.

So, what's the big deal? Well, we're using these fancy AI models called Large Language Models (LLMs) right on your own machine. No need to send your sensitive data to the cloud – privacy first, right?

Here's what FireGuardLLM can do:
- Crunch through your old firewall logs to find patterns
- Use AI to predict if something fishy is going on
- Give you a heads-up about threats in real-time
- Play nice with your existing firewall setup

The cool part is how it combines old-school data crunching with cutting-edge AI. It's like teaching an old dog new tricks, but for your firewall!

I built this because I was tired of staring at endless logs, trying to spot the needle in the haystack. With FireGuardLLM, it's like having a super-smart assistant who never sleeps.

If you're into Python and curious about how AI can beef up cybersecurity, this project is right up your alley. It's not perfect – more of a "let's see what's possible" kind of thing – but it's a start!

Want to give it a spin? Here's what you need to do:

1. Get Ollama up and running on your machine.
2. Install a few Python packages (the usual suspects: pandas, numpy, scikit-learn, and requests).
3. Grab your firewall logs and save them as 'firewall_logs.csv'. Make sure it has all the important stuff like timestamps, IPs, ports, and whether it was an attack or not.
4. Put that CSV file in the same folder as the script.
5. Run it and watch the magic happen!

Just a heads up – it might be a bit slow if you throw a ton of data at it. And yeah, the results are only as good as the AI model you're using. Play around with different ways of asking the AI about the logs; you might stumble onto something that works even better!

*Tested with Asus, and Fortinet. Good luck.

Happy hunting, and may your networks stay secure!
