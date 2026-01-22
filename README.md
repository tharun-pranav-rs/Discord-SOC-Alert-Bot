
# 🛡️ Discord SOC Alert Bot

A lightweight, automated Python agent that monitors critical web infrastructure and reports outages in real-time to a Discord Security Operations Center (SOC) channel via Webhooks.

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)

## 📸 Demo
<img width="721" height="227" alt="Screenshot 2026-01-22 111019" src="https://github.com/user-attachments/assets/8784bf71-cb52-47b5-b49c-bebf8f413845"/>


## 🚀 Features
* **Real-time Monitoring:** Checks target service availability every 60 seconds.
* **Rich Incident Reports:** Sends color-coded Embeds (Blue for Info, Red for Critical) to distinguish severity.
* **Error Handling:** Automatically detects DNS failures, timeouts, and HTTP error codes.
* **Zero-Dependency Deployment:** Can be deployed via Docker or run as a systemd service.

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Discord-SOC-Alert-Bot.git](https://github.com/YOUR_USERNAME/Discord-SOC-Alert-Bot.git)
2. Install dependencies
   pip install -r requirements.txt
3. Configure Open monitor.py and replace the WEBHOOK_URL with your own Discord Webhook.
4. Run
5. Python monitor.py
