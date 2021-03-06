from socket import *

host = 'Marcelo-Laptop'
port  = 9123

s = socket(AF_INET, SOCK_STREAM)

try: s.bind((host, port))
except error as e: print("ERROR:", e)

s.listen(1)
print('Aan het wachten voor een client.........')

conn, addr = s.accept()

print("Established Connection.\nThe client is:", addr[0]+":"+str(addr[1]))

while True:
    try:
        data = conn.recv(2048)
        print("Raspberry pi: ", data.decode("UTF-8"))
        bericht = data.decode('UTF-8')
        if bericht == 'Rotterdam: 3m':
            reply = 'rood led'
            conn.sendall(bytes(reply, "UTF-8"))

        elif bericht == 'Rotterdam: minder dan 3m':
            reply = 'groen led'
            conn.sendall(bytes(reply, "UTF-8"))
    except:
        break


print("Sorry something went wrong! You have lost connection to the client.:(")
conn.close()