import socket
import time
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/triggers/"
targets = [
    ("matt4110.com", 443, "TCP"),
    ("10.0.0.112", 443, "TCP")
]

def port_check(target, port, protocol):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        if protocol == "TCP":
            result = s.connect_ex((target, port))
            s.close()
            return result == 0
    except Exception as e:
        return result == 1
    
def send_slack_notification(target, port, protocol):
    payload = {"message": f"{target}:{port} ({protocol}) is not responding."}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

while True:
    for target, port, protocol in targets:
        if not port_check(target, port, protocol):
            send_slack_notification(target, port, protocol)
        else:
            print(f"{target}:{port} ({protocol}) is up.")
    time.sleep(60)  # Wait for 60 seconds before the next check
