import requests
import threading
import time
import os
from datetime import datetime

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

def read_urls(file_path="urls.txt"):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("Error: urls.txt not found.")
        return []

def check_url(url):
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        elapsed = round(time.time() - start, 3)
        status = f"HTTP {response.status_code}"
    except requests.RequestException as e:
        status = f"ERROR: {e}"
        elapsed = round(time.time() - start, 3)

    timestamp = datetime.now().isoformat()
    log_entry = f"[{timestamp}] {url} - {status} in {elapsed}s\n"
    print(log_entry.strip())
    append_to_log("log.txt", log_entry)

    if webhook_url and ("ERROR" in status or "HTTP" in status and int(status.split()[1]) >= 400):
        send_discord_alert(url, status)

def append_to_log(filename, text):
    with open(filename, "a") as log_file:
        log_file.write(text)

def send_discord_alert(url, status):
    message = {"content": f":warning: `{url}` is down or slow! Status: {status}"}
    try:
        requests.post(webhook_url, json=message, timeout=3)
    except requests.RequestException:
        pass  # Fail silently

def run_monitor():
    urls = read_urls()
    threads = []

    for url in urls:
        thread = threading.Thread(target=check_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("🔍 Website Uptime Monitor (Python)")
    run_monitor()
