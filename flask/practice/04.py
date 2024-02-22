# 특정 조건에 맞는 패킷 필터링, Raw 데이터 디코딩

from scapy.all import *

myFilter = "tcp port 3000"

def packet_callback(packet):
	print("\nHTTP " + myFilter+ " packet detected!")
	print(packet)
	if Raw in packet:
		raw_data = packet[Raw].load
		print("Raw data:", raw_data)
		try:
			print("Raw data (decoded):", raw_data.decode("utf-8"))
			print("Raw data (hex):", raw_data.hex())
		except UnicodeDecodeError:
			pass

sniff(prn=packet_callback, filter=myFilter)