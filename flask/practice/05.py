# 8545(Geth 기본 RPC URL) 포트 패킷 감지, Raw 데이터 디코딩

from scapy.all import *
from io import BytesIO
import gzip
import json

myFilter = "port 8545"

def decode_http_response(raw_data):
    # HTTP 헤더와 본문 분리
    header_raw, body_raw = raw_data.split(b"\r\n\r\n", 1)

    # 헤더 파싱
    headers = {}
    for line in header_raw.split(b"\r\n")[1:]:  # 첫 줄은 상태 줄이므로 제외
        key, value = line.decode().split(": ", 1)
        headers[key] = value

    # 헤더 출력
    print("Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")

    # Content-Encoding에 따른 압축 해제
    if headers.get("Content-Encoding") == "gzip":
        buf = BytesIO(body_raw)
        with gzip.GzipFile(fileobj=buf) as gz:
            decompressed_data = gz.read()
    else:
        decompressed_data = body_raw

    # 본문 데이터 디코딩 및 출력
    print("\nBody:")
    try:
        print(decompressed_data.decode("utf-8"))
    except UnicodeDecodeError as e:
        print("Error decoding body:", e)

def packet_callback(packet):
    print("\nHTTP " + myFilter + " packet detected!")
    print(packet)
    if Raw in packet:
        raw_data = packet[Raw].load
        print("Raw data:", raw_data)
        decode_http_response(raw_data)

sniff(prn=packet_callback, filter=myFilter)
