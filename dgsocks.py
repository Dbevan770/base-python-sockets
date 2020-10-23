# Import socket library
import socket

# Configure socket to be a Datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set destination IP address, currently loopback for testing but can be anything.
ipaddr = '127.0.0.1'
# Set destination port for packet
port = 10000

# Create connect at destination ip and port
s.connect((ipaddr, port))

# Send packet
s.send(b'Disturbed')

# Recieve a response from connected device
response, conn = s.recvfrom(1024)

# Decode response and print it as it is by default encoded in UTF-8
print(response.decode())
