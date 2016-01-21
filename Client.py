# Client side
import socket
import sys

HOST, PORT = "145.89.78.179", 9123
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    received = sock.recv(1024)

finally:
    sock.close()

print ("Verzonden {}".format(data))
print ("Ontvangen  {}".format(received))