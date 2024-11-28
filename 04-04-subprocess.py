import subprocess  # 외부 명령어를 실행하고 결과를 가져올 수 있는 subprocess 모듈을 임포트

# "tasklist" 명령어를 실행하여 현재 실행 중인 프로세스 목록을 가져옵니다.
output = subprocess.check_output("tasklist") 

# 명령어 실행 결과(output)는 바이트 형태로 반환되므로, 이를 'cp949' 인코딩 방식으로 디코딩하여 문자열로 변환합니다.
# 'cp949'는 한국어 윈도우에서 사용되는 문자 인코딩 방식입니다.
data = output.decode('cp949') 

# 결과 데이터를 줄 단위로 나누어 리스트로 만듭니다.
lines = data.splitlines()

# 각 줄을 하나씩 출력합니다.
for line in lines:
    print(line)

print('-------------------------------------')
# cmd 실행
import subprocess  # 외부 명령어를 실행하고 그 결과를 처리할 수 있는 subprocess 모듈을 임포트

# 'tasklist' 명령어를 실행하여 현재 실행 중인 프로세스 목록을 출력합니다.
cmd = "tasklist"
subprocess.run(cmd, shell=True)  # subprocess.run()은 명령어를 실행하고 결과를 기다립니다.

print('-------------------------------------')  # 구분선 출력


# 두 번째 명령어: 현재 디렉토리 정보 출력
import subprocess  # subprocess 모듈 다시 임포트

cmd = "cd"  # 'cd' 명령어는 현재 작업 중인 디렉토리 정보를 출력합니다.
# subprocess.run()을 사용하여 'cd' 명령어를 실행하고, 그 결과를 캡처하여 출력합니다.
result = subprocess.run(cmd, capture_output=True, shell=True, encoding='utf-8')
# capture_output=True는 명령어의 표준 출력을 캡처하여 result 객체에 저장합니다.
# encoding='utf-8'은 출력이 UTF-8로 인코딩되도록 설정합니다.

print(result.stdout)  # result.stdout에는 명령어 실행 결과가 저장되므로, 이를 출력합니다.

print('-------------------------------------')
# 출력 실시간

import subprocess  # 외부 명령어를 실행하고, 그 결과를 처리할 수 있는 subprocess 모듈을 임포트

# 실행할 명령어를 지정합니다. 여기서는 'your command to execute program' 부분을 실행하고자 하는 명령어로 바꿔야 합니다.
cmd = "your command to execute program"

# subprocess.Popen()을 사용하여 명령어를 실행합니다.
# shell=True는 셸을 통해 명령어를 실행하도록 하며,
# stdout=subprocess.PIPE는 명령어의 출력을 파이프를 통해 받을 수 있게 합니다.
# encoding='utf-8'은 출력이 UTF-8 인코딩으로 처리되도록 설정합니다.
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

# 명령어 실행 중에 실시간으로 출력 결과를 읽어옵니다.
while True:
    # process.stdout.readline()은 명령어의 출력에서 한 줄씩 읽어옵니다.
    output = process.stdout.readline()
    
    # 출력이 더 이상 없고, 프로세스가 종료되었으면 반복을 종료합니다.
    if output == '' and process.poll() is not None:
        break
    
    # 출력이 있을 경우, 그 결과를 화면에 출력합니다.
    if output:
        print(output.strip())  # strip()을 사용하여 양쪽 공백을 제거한 후 출력
