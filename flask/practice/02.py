# 특정 조건에 맞는 패킷 필터링

from scapy.all import *

myFilter = "tcp port 3000"

def packet_callback(packet):
	print("HTTP " + myFilter+ " packet detected!")
	print(packet)

sniff(prn=packet_callback, filter=myFilter)