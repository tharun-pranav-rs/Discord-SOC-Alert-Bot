import requests
import json
import datetime
import time

# ---------------- CONFIGURATION ---------------- #
# 1. Your Discord Webhook URL (Keep this secret!)
WEBHOOK_URL = ""OS_ENV_OR_PASTE_YOUR_URL_HERE"  # <--- CHANGE THIS to your Discord webhook URL!

# 2. The Website you want to monitor
TARGET_URL = "https://www.google.com"  # <--- CHANGE THIS to your Coolify app later!

# ---------------- THE ALERT FUNCTION ---------------- #
def send_security_alert(title, description, severity="INFO", ip_address="N/A"):
    """
    Sends a formatted security alert to Discord.
    """
    
    colors = {
        "INFO": 3447003,      # Blue
        "WARNING": 16776960,  # Yellow
        "CRITICAL": 15158332  # Red
    }
    
    timestamp = datetime.datetime.utcnow().isoformat()

    payload = {
        "username": "Uptime Monitor",
        "avatar_url": "https://i.imgur.com/4M34hi2.png",
        "embeds": [
            {
                "title": f"🚨 {title}",
                "description": description,
                "color": colors.get(severity, 3447003),
                "timestamp": timestamp,
                "fields": [
                    {
                        "name": "Target URL",
                        "value": f"`{TARGET_URL}`",
                        "inline": True
                    },
                    {
                        "name": "Status",
                        "value": f"**{severity}**",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "Automated Uptime Bot"
                }
            }
        ]
    }

    try:
        response = requests.post(
            WEBHOOK_URL, 
            data=json.dumps(payload), 
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 204:
            print("✅ Alert sent to Discord!")
        else:
            print(f"❌ Failed to send alert: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending webhook: {e}")

# ---------------- THE REAL MONITOR LOOP ---------------- #

print(f"🛡️ Monitoring started for: {TARGET_URL}")
print("Press Ctrl+C to stop.")

while True:
    try:
        # Check the website
        print(f"Checking {TARGET_URL}...")
        response = requests.get(TARGET_URL, timeout=10) # 10s timeout prevents hanging
        
        # Logic: If status is 200, it's good. Anything else is bad.
        if response.status_code != 200:
            print(f"⚠️ Issue detected! Status Code: {response.status_code}")
            send_security_alert(
                title="Service Outage Detected!", 
                description=f"Website returned unexpected status code: **{response.status_code}**", 
                severity="CRITICAL"
            )
        else:
            # Site is UP - stay silent on Discord, just print to console
            print(f"✅ Status 200 OK. Waiting 60 seconds...")

    except Exception as e:
        # If the site is completely unreachable (DNS error, Server Down)
        print(f"❌ Connection Failed: {e}")
        send_security_alert(
            title="Connection Failed", 
            description=f"Could not reach server. Error details: \n`{str(e)}`", 
            severity="CRITICAL"
        )

    # Sleep for 60 seconds before next check
    time.sleep(60)
