# Scapy를 이용한 패킷 생성 및 전송

from scapy.all import *

dst_ip = "127.0.0.1"
dst_port = 1234

packet = IP(dst=dst_ip) / TCP(dport=dst_port) / Raw(load="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

send(packet)