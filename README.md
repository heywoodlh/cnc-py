##cnc-py

Python reverse shell


## Server Setup:
```
git clone https://github.com/heywoodlh/cnc-py
cd cnc-py
sudo pip3 install -r requirements.txt
```

## Run Server:

`./server.py --host IP --port PORT`


## Client Setup:

Edit the variables in the beginning of `client.py` to match your desired configuration.

Then, use a Python module like `pyinstaller` or `py2exe` to create an executable of `client.py` for your desired platform and then execute the binary on the client. 
