# 🔍 py-pinger

A fast and concurrent website uptime monitor written in Python, with support for logging and optional Discord alerts.

## 🚀 Features
- Checks multiple URLs in parallel
- Logs status code and response time
- Sends alerts to a Discord webhook (optional)
- Minimal and easy to configure

## 🛠 Requirements
- Python 3.7+
- `requests` module: `pip install requests`

## 📦 Usage

1. Add URLs to `urls.txt`, one per line.

2. (Optional) Set your Discord webhook:
```bash
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
