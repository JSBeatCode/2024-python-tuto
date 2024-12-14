# argparse 모듈은 명령행에서 인자를 받아서 스크립트 동작을 다르게 설정할 수 있도록 도와줍니다.
# 예: ./run.py -d 1 -f

import argparse  # 명령행 인자를 처리하기 위한 모듈

# ArgumentParser 객체 생성
parser = argparse.ArgumentParser()

# 명령행 옵션을 추가
# -d 또는 --decimal 옵션: 값을 받아서 decimal 변수에 저장 (action="store")
parser.add_argument("-d", "--decimal", dest="decimal", action="store")

# -f 또는 --fast 옵션: 명시되면 fast 변수에 True를 저장 (action="store_true")
parser.add_argument("-f", "--fast", dest="fast", action="store_true")

# 명령행에서 입력받은 인자를 파싱하여 args에 저장
args = parser.parse_args()

# 파싱된 값 출력
print(args.decimal)  # -d 옵션으로 전달받은 값 출력
print(args.fast)     # -f 옵션이 전달되었는지 확인 (True/False)

print('-----------------------------------------------')

# 두 번째 argparse 예제

import argparse  # 다시 argparse 모듈을 사용

# ArgumentParser 객체 생성
parser1 = argparse.ArgumentParser()

# 필수 위치 인자 추가
# 위치 인자는 명령행에서 순서대로 값을 입력받아야 합니다.
parser1.add_argument(dest="width", action="store")    # 첫 번째 위치 인자: 너비
parser1.add_argument(dest="height", action="store")   # 두 번째 위치 인자: 높이

# 선택적 옵션 인자 추가
# --frames: 프레임 개수
parser1.add_argument("--frames", dest="frames", action="store")
# --qp: 품질 지수 (Quality Parameter)
parser1.add_argument("--qp", dest="qp", action="store")
# --configure: 설정 정보
parser1.add_argument("--configure", dest="configure", action="store")

# 명령행 입력을 시뮬레이션하여 파싱 (테스트용으로 리스트로 전달)
args1 = parser1.parse_args(["64", "56", "--frames", "60", "--qp", "1", "--configure", "AI"])

# 파싱된 결과 출력
print(
    args1.width,     # 위치 인자: 너비
    args1.height,    # 위치 인자: 높이
    args1.frames,    # --frames 옵션 값
    args1.qp,        # --qp 옵션 값
    args1.configure  # --configure 옵션 값
)
