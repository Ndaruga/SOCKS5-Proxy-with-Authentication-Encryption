# SOCKS5 Proxy with Authentication and Encryption

## Overview
This project is a **SOCKS5 proxy server** built with **Python**, supporting **authentication** and **AES-256 encryption** to secure communication. The proxy allows users to route internet traffic through it while ensuring secure and controlled access.

---

## 🚀 Features
- **SOCKS5 Support** - Routes both TCP and UDP traffic.
- **User Authentication** - Requires username and password to access the proxy.
- **AES-256 Encryption** - Securely encrypts authentication and transmitted data.
- **Multi-Client Support** - Handles multiple connections asynchronously.
- **Logging & Monitoring** - Tracks active connections and authentication attempts.
- **Access Control** - Can be configured to allow or restrict specific users.

---

## 🔧 Prerequisites
Before running the proxy server, ensure you have the following installed:

1. **Python 3.x** (Recommended: Python 3.8+)
   ```bash
   python3 --version
   ```
2. **Network Configuration**
   - Ensure **port 1080** is open on your local machine.
   - Adjust firewall rules if necessary.

3. **Clone the Repository**
   ```bash
   git clone https://github.com/Ndaruga/SOCKS5-Proxy-with-Authentication-Encryption.git
   cd SOCKS5-Proxy-with-Authentication-Encryption
   ```

---

## 📂 Project Structure
```
SOCKS5-Proxy-with-Authentication-Encryption/
├── proxy_server.py   # Main proxy server code
├── encryption.py     # AES-256 encryption/decryption module
├── auth.py           # User authentication system
├── config.py         # Proxy settings and user credentials
├── run-proxy-server.sh    # To run the server
└── logs/
    ├── proxy.log     # Log file for connection monitoring
```

---

## ⚙️ Configuration
Before running the proxy, update **`config.py`** to customize settings:
```python
PROXY_HOST = '0.0.0.0'  # Listen on all network interfaces
PROXY_PORT = 1080        # Default SOCKS5 port
MAX_CLIENTS = 100        # Max simultaneous connections

# Encryption settings
ENCRYPTION_KEY = b'32ByteLongSecretKeyForAES256!'  # Must be 32 bytes
ENCRYPTION_IV = b'16ByteIVForAES!!'  # Must be 16 bytes

# User credentials
USERS = {
    'user1': 'password123',
    'admin': 'securepass456'
}
```

---

## ▶️ Running the Proxy Server
1. **Clone the Repository (if applicable)**
   ```bash
   chmod u+x run-proxy-server.sh
   ./run-proxy-server.sh
   ```
2. If the server starts successfully, you should see:
   ```plaintext
   2025-02-25 12:00:00 - SOCKS5 Proxy Server started on 0.0.0.0:1080
   ```

---

## 🔍 Testing the Proxy Locally
To test if the proxy is working correctly, you can use **cURL**, **Firefox**, or a Python script.

### **1. Test with cURL**
```bash
curl --proxy socks5://user1:password123@127.0.0.1:1080 https://www.google.com
```

### **2. Test with a Python Client**
Create a new terminal within the same directory `SOCKS5-Proxy-with-Authentication-Encryption`
Ensure that the virtual environment is acivated in the new terminal

```bash
source venv/bin/activate
```
Run the client script:

```bash
python3 proxy_client.py
```
You will be prompted to enter the username and password.

you can use username `admin` and password `securepass456`


---

## 📜 Logging & Monitoring
All connections and authentication attempts are logged in **logs/proxy.log**.
To monitor logs in real time:
```bash
tail -f logs/proxy.log
```
This helps in debugging and tracking activity.

---

## ❗ Troubleshooting
### **1. Proxy Not Connecting?**
- Ensure **port 1080 is open** using:
  ```bash
  sudo netstat -tulnp | grep 1080
  ```
- Check **firewall settings** to allow connections.

### **2. Authentication Fails?**
- Verify **username and password** in `config.py`.
- Restart the server and try again.

### **3. Can't Access HTTPS Sites?**
- Ensure your client **supports SOCKS5 proxies** (not just HTTP/HTTPS proxies).

---

## 🚀 Deployment
To Deploy this Proxy on a cloud platform like **AWS**, Consider checking out the [Deployment instructions](https://github.com/Ndaruga/SOCKS5-Proxy-with-Authentication-Encryption/blob/main/Deployment.md)

---

## ✅ Next Steps
- **Enhance security**: Implement IP whitelisting.
- **Improve performance**: Optimize multi-client handling.
- **Expand functionality**: Add UDP support.

---

## 📝 License
This project is licensed under the MIT License.

---

## 🤝 Contributions
Feel free to fork the repository and submit pull requests to improve functionality!

