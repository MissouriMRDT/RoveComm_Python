from RoveComm_Python import RoveCommEthernetUdp
import struct
local_host_ip = "127.0.0.1"
RoveComm = RoveCommEthernetUdp()
RoveComm.writeTo(10, 11, struct.pack('L', 7), local_host_ip)
data_id, data_size, data = RoveComm.read()

print(data_id, data_size, struct.unpack('L', data))

RoveComm.write(4, 11, struct.pack('L', 7))
data_id, data_size, data = RoveComm.read()
print(data_id, data_size, struct.unpack('L', data))
print(RoveComm.subscribers)

RoveComm.writeTo(10, 11, struct.pack('L', 7), local_host_ip)

