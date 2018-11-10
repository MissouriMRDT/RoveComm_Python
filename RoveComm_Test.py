from RoveComm_Python import *
import struct
import random
import time
test_board_ip = "192.168.1.141"
RoveComm = RoveCommEthernetUdp()
count = 0
sleep_time = (.100)
#Test Data IDs
#subscribe
count = count + 1
packet = RoveCommPacket(1, 'b', (1,), '141')
time.sleep(1)
RoveComm.write(packet)

''' Python Read
print("Count, Data ID, Data Count, Data")
count = 0
while(1):
	packet = RoveComm.read()
	if (packet.data_id != 0):
		count = count +1
		print(count, ",", packet.data_id, ",",packet.data_count, ",",packet.data)
'''		


''' Python Write Code
print(count, ",", 1000,",", 1,",", 1)
count = count + 1
packet = RoveCommPacket(2000, 'b', (1,), '141')
RoveComm.write(packet)
time.sleep(sleep_time)
print(count, ",", 2000,",", 1,",", 1)
count = count + 1
packet = RoveCommPacket(3000, 'b', (1,), '141')
RoveComm.write(packet)
time.sleep(sleep_time)
print(count, ",", 3000,",", 1,",", 1)
count = count + 1
packet = RoveCommPacket(65000, 'b', (1,), '141')
RoveComm.write(packet)
time.sleep(sleep_time)
print(count, ",", 65000,",", 1,",", 1)
count = count + 1
for i in range(1, 5):
	time.sleep(sleep_time)
	random_num = random.randint(0, 10000)
	packet = RoveCommPacket(random_num, 'b', (1,), '141')
	RoveComm.write(packet)
	print(count, ",", random_num,",", 1,",", 1)
	count = count + 1

#Test Data Types
	
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(-127, 127)
	random_num2 = random.randint(-127, 127)
	random_num3 = random.randint(-127, 127)
	packet = RoveCommPacket(10, 'b', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(0, 255)
	random_num2 = random.randint(0, 255)
	random_num3 = random.randint(0, 255)
	packet = RoveCommPacket(10, 'B', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(-32768,3267)
	random_num2 = random.randint(-32768,3267)
	random_num3 = random.randint(-32768,3267)
	packet = RoveCommPacket(10, 'h', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(0, 65535)
	random_num2 = random.randint(0, 65535)
	random_num3 = random.randint(0, 65535)
	packet = RoveCommPacket(10, 'H', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(-200000000, 2000000000)
	random_num2 = random.randint(-200000000, 2000000000)
	random_num3 = random.randint(-200000000, 2000000000)
	packet = RoveCommPacket(10, 'l', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
for i in range(0, 10):
	time.sleep(sleep_time)
	random_num1 = random.randint(0, 4000000000)
	random_num2 = random.randint(0, 4000000000)
	random_num3 = random.randint(0, 4000000000)
	packet = RoveCommPacket(10, 'L', (random_num1,random_num2, random_num3), '141')
	RoveComm.write(packet)
	print(count, ",", 10,",", 3,",", random_num1,",",random_num2,",",random_num3)
	count = count + 1
'''
	