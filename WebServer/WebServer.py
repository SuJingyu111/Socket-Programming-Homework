# import socket module
from socket import *
import time
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()# Fill in start #Fill in end
    try:
        message =  connectionSocket.recv(1024).decode()# Fill in start #Fill in end
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read() # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
    # Send response message for file not found
    # Fill in start
        header = ' HTTP/1.1 404 Not Found'
        print('here')
        connectionSocket.send(header.encode())
    # Fill in end
    # Close client socket
    # Fill in start
        connectionSocket.close()
    # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data