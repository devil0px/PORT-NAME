import socket
while True:
    port = int(input('Enter por : '))
    test = socket.getservbyport(port)
    print(test)
          
