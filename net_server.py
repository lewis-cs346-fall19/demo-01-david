#server file
import socket
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    addr = (host, 24611)
    sock.bind(addr)

    sock.listen(5)
    connectedSock, clientAddress = sock.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting'+ "\n"
    connectedSock.send(msg.encode('ascii'))
    while True:
        try:
            msg = connectedSock.recv(1024).decode()
            msg = msg[::-1]
            connectedSock.send(msg.encode('ascii'))
        except:
            sock.close()

main()
