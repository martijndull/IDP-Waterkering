import socket

def server():
    HOST = socket.gethostname()
    PORT = 9123

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))

    print (HOST)

    sock.listen(5)

    while True:
        (c, addr) = sock.accept()
        print ('gelukt', addr)
        c.close

    while True:
        data = sock.recv()
        print (data)


server()
