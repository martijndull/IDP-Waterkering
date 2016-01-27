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

rotterdam = 'laag'
dordrecht = 'laag'

while True:
    try:

        print ("start")
        data = conn.recv(2048)
        bericht = data.decode('UTF-8')

        print ("bericht: " + bericht)

        #Rotterdam
        if bericht == 'Rotterdam: 3m':
            rotterdam = 'hoog'
            bestand = open('waterstandrotterdam.txt', 'w')
            bestand.write("hoog")
            bestand.close()
            reply = 'rood led'
            conn.sendall(bytes(reply, "UTF-8"))
            print (rotterdam)

        if bericht == 'Rotterdam: minder dan 3m':
            rotterdam = 'laag'
            bestand = open('waterstandrotterdam.txt', 'w')
            bestand.write("laag")
            bestand.close()
            print (rotterdam)
            if dordrecht == 'hoog' and rotterdam == 'laag':
                reply = 'niks'
                conn.sendall(bytes(reply, "UTF-8"))
            elif dordrecht == 'laag' and rotterdam == 'laag':
                print('test3')
                reply = 'groen led'
                conn.sendall(bytes(reply, "UTF-8"))

        #Dordrecht

        if bericht == 'Dordrecht: 3m':
            dordrecht = 'hoog'
            bestand = open('waterstanddordrecht.txt', 'w')
            bestand.write("hoog")
            bestand.close()
            reply = 'rood led'
            conn.sendall(bytes(reply, "UTF-8"))
            print (dordrecht)

        if bericht == 'Dordrecht: minder dan 3m':
            dordrecht = 'laag'
            bestand = open('waterstanddordrecht.txt', 'w')
            bestand.write("laag")
            bestand.close()
            print (dordrecht)
            if rotterdam == 'hoog' and dordrecht == 'laag':
                reply = 'niks'
                conn.sendall(bytes(reply, "UTF-8"))
            elif rotterdam == 'laag' and dordrecht == 'laag':
                print('test4')
                reply = 'groen led'
                conn.sendall(bytes(reply, "UTF-8"))

        print ("end")

    except:
        print ("Hier gaat t mis")
        break


print("Sorry something went wrong! You have lost connection to the client.:(")
conn.close()
