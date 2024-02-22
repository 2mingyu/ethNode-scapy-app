import gzip
import json

# 압축된 데이터 추출 (HTTP 헤더를 제외한 부분)
compressed_data = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\x04\xc0A\n\xc20\x10\x05\xd0\xbd\xa7\x08\x7f\x1d%\xc4\xdd\\E\\\xb4\xc9WGZ\x13f"(\xa5w\xef\xbbmx{\xfbX/\x10\xe4KB\x84VH\x8e\xa0Y3\xc8\x86\xd2*!\xe7kN)E\xact\x9f\x9e\x84\x80\xe3E\x9b\'gX\xbf>\xc2\xcc\xc0__\xb4\xe8X\xfe\xc1;\x8b>\x94\x15\xfb~?\x1d\x01\x00\x00\xff\xff\xf0\x0f\x84_f\x00\x00\x00'

# gzip 압축 해제
try:
    decompressed_data = gzip.decompress(compressed_data)
    print("Decompressed data:", decompressed_data)

    # JSON 파싱 시도
    try:
        json_data = json.loads(decompressed_data)
        print("JSON data:", json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Decompressed data is not valid JSON.")
except OSError as e:
    print("Error decompressing data:", e)