python3 -m venv venv
source venv/bin/activate
echo Installing Libraries... ✅
pip install --no-cache-dir -r requirements.txt
echo Starting proxy server... ✅
python3 proxy_server.py