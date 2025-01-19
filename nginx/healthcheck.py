import sys
import socket

def healthcheck():
    try:
        host = "localhost"
        port = 8000
        with socket.create_connection((host, port), timeout=5):
            return True
    except Exception:
        return False

if __name__ == "__main__":
    if healthcheck():
        sys.exit(0)
    else:
        sys.exit(1)
