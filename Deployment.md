# Deploying the SOCKS5 Proxy on AWS EC2

## 🚀 Overview
This guide provides step-by-step instructions on deploying the **SOCKS5 proxy with authentication and encryption** on an AWS EC2 instance.

---

## ✅ Prerequisites
Before deployment, ensure you have:
- **AWS Account** with access to launch EC2 instances.
- **Basic Linux Knowledge** (Ubuntu or Amazon Linux preferred).
- **SSH Key Pair** for secure access to the EC2 instance.
- **Python 3.x Installed** (EC2 comes with Python pre-installed).

---

## 🔧 Step 1: Launch an EC2 Instance
1. **Log in to AWS** and go to the **EC2 Dashboard**.
2. Click **Launch Instance**.
3. Choose an **Amazon Machine Image (AMI)**:
   - **Ubuntu 22.04 LTS** (Recommended)
   - **Amazon Linux 2** (Alternative)
4. Select an **Instance Type** (Recommended: `t2.micro` for testing, `t3.small` or higher for production).
5. Configure **Security Group**:
   - Allow **Inbound Rule** for **TCP Port 1080** (SOCKS5 Proxy)
   - Allow **TCP Port 22** for SSH access.
   - (Optional) Restrict access to your **trusted IPs only**.
6. Add **Storage** (default 8GB is enough).
7. Choose an **SSH Key Pair** or create a new one.
8. Click **Launch** and wait for the instance to initialize.

---

## 🖥️ Step 2: Connect to the EC2 Instance
Once the instance is running, connect via SSH:
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```
For Amazon Linux, use:
```bash
ssh -i your-key.pem ec2-user@your-ec2-public-ip
```

---

## 📥 Step 3: Clone the SOCKS5 Proxy Repository
```bash
git clone https://github.com/Ndaruga/SOCKS5-Proxy-with-Authentication-Encryption.git
cd SOCKS5-Proxy-with-Authentication-Encryption
```
   > You can choose to skip to **step 7** by running the command `sudo chmod u+x run-proxy-server.sh && ./run-proxy-server.sh`
---

## 🔥 Step 4: Install Dependencies
Update the system and install required packages:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
```
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Step 5: Configure the Proxy
Edit the `config.py` file:
```bash
nano config.py
```
Update the following settings:
```python
PROXY_HOST = '0.0.0.0'  # Listen on all interfaces
PROXY_PORT = 1080        # Default SOCKS5 Port

USERS = {
    'user1': 'password123',
    'admin': 'securepass456'
}
```
Save the file and exit.

---

## ▶️ Step 6: Run the Proxy Server
Start the proxy server:
```bash
python3 proxy_server.py
```
If successful, you should see:
```plaintext
SOCKS5 Proxy Server started on 0.0.0.0:1080
```

---

## 🌐 Step 7: Configure a Client to Connect
### **Option 1: Mobile Phone**
1. Depending on the device, Open **Device Settings > WI-Fi**.
2. Select the Wifi you are connected to and click on **More** or the **info Icon**
3. Select **Proxy** and change the configuration to **Manual**
4. In the **server/host**, Enter the EC2 **Public IP** and under port, enter **1080**.
5. Enable authentication and use any of the following combinations
   | username | Password      |
   |----------|---------------|
   | admin    | securepass456 |
   | user1    | password123   |
6. Save the configuration and open any browser on the Device. Visiting [whatismyipaddress.com](https://www.whatismyipaddress.com).

   > ***Proxy configuration for this method only works when the device is connected to the internet via Wi-Fi***


### **Option 2: Firefox**
1. Open **Firefox > Settings > Network Settings**.
2. Select **Manual Proxy Configuration**.
3. Enter the EC2 **Public IP** and **Port 1080**.
4. Enable **SOCKS v5** and **Proxy DNS when using SOCKS v5**.
6. Save and test by visiting [whatismyipaddress.com](https://www.whatismyipaddress.com).
7. When prompted to Enter username and password, use any combinations below
   | username | Password      |
   |----------|---------------|
   | admin    | securepass456 |
   | user1    | password123   |

### **Option 3: Using cURL**
Run the following command on your local machine:
```bash
curl --proxy socks5://user1:password123@your-ec2-public-ip:1080 https://www.google.com
```

---

## 🛠️ Step 8: Run Proxy in the Background (Optional)
To keep the proxy running after logout, use:
```bash
nohup python3 proxy_server.py > proxy.log 2>&1 &
```
Check logs:
```bash
tail -f proxy.log
```

---

## 🔐 Step 9: Secure the Proxy
Since your proxy is **open to the internet**, restrict access to trusted IPs:
```bash
sudo ufw allow from YOUR_IP to any port 1080
sudo ufw enable
```
To check firewall rules:
```bash
sudo ufw status
```

---

## ✅ Final Step: Verify Everything Works
- Check **logs** for connections:
  ```bash
  tail -f logs/proxy.log
  ```
- Confirm **your public IP changes** when browsing through the proxy.
- Test different **clients (cURL, Firefox, mobile devices)** to ensure connectivity.

---

## 🎯 Next Steps
- **Automate deployment** using AWS **EC2 User Data** or Terraform.
- **Enhance security** by enforcing **TLS encryption**.
- **Scale up** with multiple proxies in different regions.

---

## 📝 License
This project is licensed under the MIT License.

---

## 🤝 Contributions
Pull requests and improvements are welcome!

