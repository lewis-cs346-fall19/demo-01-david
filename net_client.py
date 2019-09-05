"""
    client file
"""

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    addr = (host, 24611)

    sock.connect(addr)
    in_msg = sock.recv(1024)
    print(in_msg)
    user = input()
    while(user.lower() != "n"):
        sock.sendall(user.encode('utf-8'))
        in_msg = sock.recv(1024)
        print(in_msg)
        user = input()
    sock.close()
main()

