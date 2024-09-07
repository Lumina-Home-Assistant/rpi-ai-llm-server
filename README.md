### Requirements

- Python 3.8+ or higher
- PIP (if you have python you most likely already have this installed)
- At least 8 gigs of RAM

> **Make sure to create a python virtual environment before installing the dependencies**

```shell
git clone https://www.github.com/Zachary-Richman/rpi-ai-llm-server
pip install -r requirements.txt
python app.py
```

then go to [localhost:5000/llmcontext/prompt](http://127.0.0.1:5000/you%20are%20a%20duck/talk%20to%20me%20in%20duck)

Depending on your machine the speed at which you get a response may vary. This server is now running on your network and can be accesed by any device on it (simply obtain your net-ipaddress)

In PowerShell `Get-NetIPAddress`