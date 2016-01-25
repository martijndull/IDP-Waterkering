from socket import *
import time

host = 'SERVER1'
port = 9123

s = socket(AF_INET, SOCK_STREAM)

def conct ():
    s.connect((host, port))

while True:
    print("Trying to connect to:", host + ":" + str(port))
    try:
        conct()
        break
    except:
        print("There is no Server at:", host + ":" + str(port))
        print("Trying again in 5 Seconds\n")
        time.sleep(5)
        pass


print("Connection To Server Established!\nThe server is:", host+":"+str(port))

while True:
    try:
        msg = input("Raspberry pi: ")
        s.send(bytes(msg, "UTF-8"))

        reply = s.recv(2048)
        print(host, reply.decode("UTF-8"))
    except:
        break



print("Sorry something went wrong! You have lost connection to the server.:(")
input("")

s.close()