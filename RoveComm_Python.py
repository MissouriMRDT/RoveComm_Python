import socket
import struct

'''
local_host_ip = "127.0.0.1"
test_var = 0xff

test_byte = struct.pack('L', test_var)

RoveCommSocket = socket.socket(type = socket.SOCK_DGRAM)
RoveCommSocket.bind(("", 11000))

RoveCommSocket.sendto(test_byte, (local_host_ip, 11000))

bytes, address = RoveCommSocket.recvfrom(1024)
print (test_byte)
print (bytes, address)
print (struct.unpack('L', test_byte))
'''
ROVECOMM_PORT = 11000

class RoveCommEthernetUdp:
	def __init__(self, port=ROVECOMM_PORT):
		self.rove_comm_port = rove_comm_port
		self.subscribers = []
		self.last_data_id    = 0
		self.last_data_value = 0
		self.last_data_size  = 0 #RC2: add last_data_type, last_data_count
		
		self.RoveCommSocket = socket.socket(type = socket.SOCK_DGRAM)
		self.RoveCommSocket.bind(("", port))
		
	def write(  data_id, data_size, data) #RC2: add data_type, data_count
	
	def read()
	
	def writeTo(data_id, data_size, data, ip_address, port=ROVECOMM_PORT) #RC2: add data_type, data_count
	
	#def readFrom ToDo: Change to getLastIp for C++ and Python
	
