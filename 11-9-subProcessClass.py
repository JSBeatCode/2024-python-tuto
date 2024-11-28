# 주요 학습 포인트:
# 1. 메모리 독립성: 멀티프로세싱은 각 프로세스가 독립적인 메모리 공간을 가지므로, 
# 한 프로세스에서 변경된 변수는 다른 프로세스에 영향을 주지 않습니다.
# 2. 프로세스 상태: is_alive()와 join()을 사용하여 프로세스의 실행 상태를 확인하고 동기화할 수 있습니다.
# 3. 다른 프로세스에서 클래스 메서드 호출: target으로 클래스 메서드를 지정할 수 있으며, 
# 인스턴스는 독립적으로 작동합니다.

import multiprocessing as mp

class Worker:
    def __init__(self):
        print("__init__", mp.current_process().name)