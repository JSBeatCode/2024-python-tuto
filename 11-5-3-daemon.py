import multiprocessing as mp  # 멀티프로세싱 모듈을 가져옵니다.
import time  # 시간 지연 처리를 위해 time 모듈을 가져옵니다.

# 서브 프로세스에서 실행할 작업 함수 정의
def work():
    print("Sub Process Start")  # 서브 프로세스가 시작되었음을 출력합니다.
    time.sleep(2)  # 2초 동안 작업을 수행합니다.
    print("Sub Process End")  # 서브 프로세스가 종료되었음을 출력합니다.

# 메인 실행 블록
if __name__ == "__main__":
    print("Main Process Start")  # 메인 프로세스가 시작되었음을 출력합니다.

    # 서브 프로세스 생성
    proc = mp.Process(
        name="Sub Process",  # 서브 프로세스의 이름을 지정합니다.
        target=work,         # 실행할 함수(work)를 지정합니다.
        daemon=True          # 서브 프로세스를 데몬 프로세스로 설정합니다.
    )

    proc.start()  # 서브 프로세스를 시작합니다. `work` 함수가 실행됩니다.

    print("Main Process End")  # 메인 프로세스의 작업이 종료되었음을 출력합니다.

# 주요 포인트:
# 1. 데몬 프로세스(daemon=True):
#    - 데몬 프로세스는 메인 프로세스가 종료되면 즉시 강제 종료됩니다.
#    - 메인 프로세스의 수명에 의존하며, 독립적으로 실행되지 않습니다.
#    - 위 코드에서 메인 프로세스가 "Main Process End"를 출력한 후 종료되므로,
#      서브 프로세스는 작업을 끝마치지 못하고 강제 종료됩니다.
#
# 2. 실행 흐름:
#    - "Main Process Start" 출력.
#    - 서브 프로세스 시작, "Sub Process Start" 출력.
#    - 메인 프로세스는 "Main Process End"를 출력하고 종료.
#    - 서브 프로세스는 메인 프로세스 종료와 함께 작업을 끝마치지 못하고 강제 종료.
