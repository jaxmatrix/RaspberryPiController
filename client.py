import socket

ip = str(raw_input("Enter ip to connect:"))
msgFromClient = "Hello UDP Server"
serverAddressPort = (ip,20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


#Send to server using created UDP socket
while True:
    msgFromClient = str(raw_input("Enter the message:"))
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend,serverAddressPort)
    msgFromServer =  UDPClientSocket.recvfrom(bufferSize)
    msg = "Message From Server{}".format(msgFromServer[0])
    print(msg)


