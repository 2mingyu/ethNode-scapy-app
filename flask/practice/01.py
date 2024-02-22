# 패킷 감지 예제

from scapy.all import *

def packet_callback(packet):
	print("packet detected!")
	print(packet.show())

sniff(prn=packet_callback, count=10)