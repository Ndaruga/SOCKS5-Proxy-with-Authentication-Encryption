rm -rf __pycache__ venv logs/proxy.log && touch logs/proxy.log
sudo apt-get update
sudo apt install python3.12-venv
sudo kill -9 $(sudo lsof -t -i:1080)
python3 -m venv venv
source venv/bin/activate
echo Installing Libraries... ✅
pip install --no-cache-dir -r requirements.txt
clear
echo Starting proxy server... ✅
python3 proxy_server.py
