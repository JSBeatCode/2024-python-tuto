print('------------------------------------------------------')

# 데이터 압축 예제
import zlib  # 데이터 압축 및 압축 해제 기능을 제공하는 zlib 모듈 임포트

# 바이트 문자열을 정의합니다.
s = b'witch which has which witches wrist watch'
rs = len(s)  # 원본 데이터의 길이를 계산합니다.
print(rs)  # 원본 데이터의 길이를 출력합니다.

# 데이터를 압축합니다.
t = zlib.compress(s)
rs1 = len(t)  # 압축된 데이터의 길이를 계산합니다.
print(rs1)  # 압축된 데이터의 길이를 출력합니다.

# 압축된 데이터를 해제하여 원본 데이터로 복원합니다.
rs2 = zlib.decompress(t)
print(rs2)  # 복원된 데이터(원본)를 출력합니다.

# 원본 데이터의 CRC32 체크섬 값을 계산합니다.
rs3 = zlib.crc32(s)
print(rs3)  # CRC32 체크섬 값을 출력합니다.