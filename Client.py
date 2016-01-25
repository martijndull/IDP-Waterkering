import socket
from _thread import *

def client():
 HOST = 'SERVER1'
 PORT = 9123
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((HOST, PORT))

 data = s.recv(2048)
 print("Recieved: "+(data.decode('utf-8')))

 def threaded_client(conn):

  while True:
   data = conn.recv(2048)
   print(data.decode('utf-8'))
   reply = 'Client output: '+data.decode('utf-8')
   conn.sendall(str.encode(reply))

  start_new_thread(threaded_client,(conn,))



client()