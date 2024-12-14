# 2. Join

import multiprocessing as mp  # 멀티프로세싱 모듈을 가져옵니다.
import time  # 시간 지연을 위해 time 모듈을 가져옵니다.

# 서브 프로세스에서 실행할 작업 함수 정의
def work():
    print("Sub Process Start")  # 서브 프로세스가 시작되었음을 출력합니다.
    time.sleep(2)  # 2초 동안 작업을 수행하는 것으로 시뮬레이션합니다.
    print("Sub Process End")  # 서브 프로세스가 종료되었음을 출력합니다.

# 메인 실행 블록
if __name__ == "__main__":
    print("Main Process Start")  # 메인 프로세스가 시작되었음을 출력합니다.

    # 서브 프로세스를 생성합니다.
    proc = mp.Process(
        name="Sub Process",  # 생성되는 서브 프로세스의 이름을 지정합니다.
        target=work          # 실행할 함수(work)를 지정합니다.
    )

    proc.start()  # 서브 프로세스를 시작합니다. `work` 함수가 실행됩니다.

    # `join` 메서드는 메인 프로세스가 서브 프로세스의 종료를 기다리게 만듭니다.
    proc.join()  # 서브 프로세스가 종료될 때까지 대기합니다.

    print("Main Process End")  # 서브 프로세스가 종료된 이후 출력됩니다.

# 코드 실행 순서:
# 1. "Main Process Start" 출력.
# 2. 서브 프로세스 시작, "Sub Process Start" 출력.
# 3. 메인 프로세스는 `proc.join()`에 의해 서브 프로세스가 종료될 때까지 대기.
# 4. 서브 프로세스에서 2초 대기 후 "Sub Process End" 출력.
# 5. 서브 프로세스 종료 후, 메인 프로세스가 다시 실행되고 "Main Process End" 출력.
