# 1. 기본 프로세스 동작

import multiprocessing as mp  # 멀티프로세싱 모듈을 가져옵니다.
import time  # 시간 지연을 위해 time 모듈을 가져옵니다.

# 실행될 작업 함수 정의
def work():
    print("Sub Process Start")  # 서브 프로세스가 시작되었음을 출력합니다.
    time.sleep(2)  # 2초 동안 대기합니다.
    print("Sub Process End")  # 서브 프로세스가 종료되었음을 출력합니다.

# 메인 실행 블록
if __name__ == "__main__":
    # 파이썬 스크립트가 직접 실행될 때만 실행되도록 설정 (멀티프로세싱에서 필수)
    print("Main Process Start")  # 메인 프로세스가 시작되었음을 출력합니다.

    # 서브 프로세스를 생성합니다.
    proc = mp.Process(
        name="Sub Process",  # 프로세스 이름을 지정합니다.
        target=work          # 실행할 작업 함수를 지정합니다.
    )

    proc.start()  # 서브 프로세스를 시작합니다. `work()` 함수가 호출됩니다.

    print("Main Process End")  # 메인 프로세스가 종료되었음을 출력합니다.
    # 메인 프로세스는 서브 프로세스가 종료되기를 기다리지 않고 실행을 계속합니다.

# 이 코드의 흐름:
# 1. "Main Process Start"가 출력됩니다.
# 2. 서브 프로세스가 시작되고 "Sub Process Start"가 출력됩니다.
# 3. 메인 프로세스는 "Main Process End"를 출력하고 종료됩니다.
# 4. 서브 프로세스는 2초 대기 후 "Sub Process End"를 출력합니다.
