#!/usr/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax Error. Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <IP Address>")

print('*' * 50)
print(f"Scanning {target}")
print(f"Time started: {datetime.now()}")
print('*' * 50)

try:
    for port in range(50,85):
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = _socket.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open.")
        _socket.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
