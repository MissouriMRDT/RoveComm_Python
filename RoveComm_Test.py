python
from RoveComm_Python import *
import struct
local_host_ip = "127.0.0.1"
test_board_ip = "192.168.1.141"
RoveComm = RoveCommEthernetUdp()

packet = RoveCommPacket(1, 'b', (3, 4, 5, 6), '141')
RoveComm.write(packet)

packet2 = RoveCommPacket()
packet2 = RoveComm.read()
packet2.print()

'''
packet = RoveCommPacket(10, 'b', (3, 4, 5, 6))
packet2 = RoveCommPacket()
packet.SetIp(local_host_ip)
packet.print()
RoveComm = RoveCommEthernetUdp()
RoveComm.write(packet)
packet2 = RoveComm.read()
packet2.print()
quit()

data_id, data_size, data = RoveComm.read()

print(data_id, data_size, struct.unpack('L', data))

RoveComm.write(4, 11, struct.pack('L', 7))
data_id, data_size, data = RoveComm.read()
print(data_id, data_size, struct.unpack('L', data))
print(RoveComm.subscribers)

RoveComm.writeTo(10, 11, struct.pack('L', 7), local_host_ip)

conda activate RoveComm_Python
cd C:\Users\andre\Documents\Rover\GitHub\Libraries\RoveComm_Python
cd C:\Users\andre\Documents\Rover\GitHub\Software\RoveComm_Tester_Software\PINK

from Sender import *
test = sendWidget()
'''