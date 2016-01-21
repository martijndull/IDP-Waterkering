

#Server side
import socketserver

class MijnTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("{}...gelukt".format(self.client_address[0]))
        print (self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "IDPG2", 9123
    server = socketserver.TCPServer((HOST, PORT), MijnTCPHandler)

    server.serve_forever()
