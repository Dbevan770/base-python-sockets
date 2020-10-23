# Import socket library
import socket

# Configure stream socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set destination IP address, currently loopback can be changed to anything.
ipaddr = '172.16.1.15'
# Specify port used by the packet
port = 5309

# Create socket connection
s.connect((ipaddr, port))

# Send packet with message
s.send(b'Jenny')

# Recieve a response from connection
response, conn = s.recvfrom(1024)

# Decode the response as it is by default encoded with UTF-8
print(response.decode())

# Close the connection/ graceful teardown
s.close()
