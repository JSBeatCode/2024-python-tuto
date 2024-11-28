import threading  # threading 모듈을 가져옵니다. 이 모듈을 사용하면 스레드를 생성하고 관리할 수 있습니다.
import time       # time 모듈은 일정 시간 동안 실행을 멈추거나 시간과 관련된 기능을 제공합니다.

# Worker 클래스 정의 - threading.Thread 클래스를 상속받아 스레드를 구현
class Worker(threading.Thread):
    def __init__(self, name):
        # 부모 클래스인 threading.Thread의 초기화 메서드 호출
        super().__init__()
        self.name = name  # 스레드의 이름을 설정합니다.

    # 스레드 실행 시 호출되는 메서드 (threading.Thread 클래스의 run 메서드를 오버라이드)
    def run(self):
        # 현재 실행 중인 스레드의 이름을 출력합니다.
        print("sub thread start ", threading.current_thread().name)
        time.sleep(3)  # 3초 동안 실행을 멈춥니다.
        # 스레드 작업이 끝났음을 알리며 현재 스레드의 이름을 출력합니다.
        print("sub thread end ", threading.current_thread().name)

# 메인 스레드 시작
print("main thread start")

# 총 5개의 Worker 스레드를 생성하고 실행합니다.
for i in range(5):
    # 각 스레드에 고유한 이름을 부여합니다.
    name = "thread {}".format(i)
    t = Worker(name)  # Worker 객체(스레드) 생성
    t.start()  # 스레드 실행 (실제 실행은 run 메서드에 의해 이루어짐)

# 메인 스레드 작업 종료
print("main thread end")

"""
1. threading 모듈:
Python에서 스레드를 생성하고 관리하기 위해 제공되는 표준 라이브러리입니다.
threading.Thread 클래스를 상속받아 사용자 정의 스레드를 생성할 수 있습니다.

2. Worker 클래스:
threading.Thread를 상속받아 새로운 스레드 동작을 정의하는 클래스입니다.
__init__ 메서드: 부모 클래스의 초기화 메서드를 호출한 뒤, 스레드 이름을 설정합니다.
run 메서드: 스레드가 실행될 때 호출되는 메서드로, 스레드의 주요 작업이 여기에 정의됩니다.

3. 메인 스레드와 서브 스레드:
for 루프에서 5개의 Worker 객체를 생성하고 start()를 호출하여 실행합니다.
start() 메서드는 내부적으로 run() 메서드를 호출합니다.
각 서브 스레드는 3초 동안 대기 후 작업이 완료됩니다.

4. 출력 설명:
"main thread start"와 "main thread end"는 메인 스레드의 작업입니다.
각 서브 스레드는 독립적으로 동작하며, 실행 순서는 비결정적(비동기)입니다.
각 스레드는 "sub thread start"와 "sub thread end"를 출력하며 자신의 이름도 함께 표시합니다.
"""