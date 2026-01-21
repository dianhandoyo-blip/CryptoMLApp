import hashlib
from datetime import datetime

LOG_FILE = "security.log"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def write_log(event):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {event}\n")

def get_stats():
    stats = {"encrypt":0,"decrypt":0,"failed":0}
    try:
        with open(LOG_FILE) as f:
            for line in f:
                if "ENCRYPT" in line: stats["encrypt"]+=1
                elif "DECRYPT_FAILED" in line: stats["failed"]+=1
                elif "DECRYPT" in line: stats["decrypt"]+=1
    except:
        pass
    return stats
