#import calls
from socket import *
import sys

#initiate Socket and Port
serverSocket= socket(AF_INET,SOCK_STREAM)
serverPort=6789
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)

#establish a connection to the server
while True:
    print('Ready to serve...')
    connectionSocket,addr= serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message.decode())
        filename = message.split()[1]

        if filename.decode()=='/grades/students.html':
            connectionSocket.send('HTTP/1.0 403 Forbidden\r\n\r\n403 Forbidden'.encode())
            connectionSocket.send('\r\n'.encode())
            serverSocket.close()
        elif filename.decode()=='/grades/':
            connectionSocket.send('HTTP/1.0 403 Forbidden\r\n\r\n403 Forbidden'.encode())
            connectionSocket.send('\r\n'.encode())
            serverSocket.close()
        else:
        #fill in security code
            f= open(filename[1:])

        #Read data in from file
            outputdata=f.read()

        #fill in code to send header
        #connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n ".encode())
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            connectionSocket.send('\r\n'.encode())

            for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()



    except IOError:
        print("sent error")
        connectionSocket.send('HTTP/1.1 404 Not Found \r\n\r\n 404 Not Found'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()


