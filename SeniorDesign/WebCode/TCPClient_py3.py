
from socket import *
serverName = "137.140.180.233"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
#sentence = input("Input lowercase sentence: ")
sentence = "trouble"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("%s: %s" % ("From  Server ", modifiedSentence.decode()))

clientSocket.close()

