import os 
import socket
import bluetooth 
from bluetooth import* 
from itertools import count 
#devices = discover_devices() 
#print(devices)
os.system("sudo hciconfig hci0 piscan")
msgFromClient = "takeoff"
#for i in count(0):
port = 1
# create a Bluetooth server socket
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", port))
server_socket.listen(1)       
client_socket, address = server_socket.accept()
# receive the command
data = client_socket.recv(1024)
# print the command
print('Received command:', data.decode())


msgFromClient = data.decode()
def command_input(command_input):
          bytesToSend         = str.encode(msgFromClient)
          serverAddressPort   = ("192.168.10.1",8889) 
          bufferSize          = 1024
          # Create a UDP socket at client side
          UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
          # Send to server using created UDP socket
          UDPClientSocket.sendto(bytesToSend, serverAddressPort)
          msgFromServer = UDPClientSocket.recvfrom(bufferSize)
          msg = "Message from Server {}".format(msgFromServer[0])
          print(msg)
command_input(msgFromClient)
os.system("pkill -9 -f Recv_bluetooth.py")
