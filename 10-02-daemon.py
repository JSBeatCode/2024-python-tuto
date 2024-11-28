import threading  # 스레드를 생성하고 관리하기 위해 threading 모듈을 가져옵니다.
import time       # 시간 관련 기능을 제공하는 time 모듈을 가져옵니다.

# Worker 클래스 정의 - threading.Thread 클래스를 상속받아 사용자 정의 스레드 구현
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()  # 부모 클래스의 초기화 메서드를 호출하여 스레드 설정
        self.name = name  # 스레드의 이름을 설정합니다.

    # 스레드가 실행될 때 호출되는 메서드 (run 메서드 오버라이드)
    def run(self):
        print("sub thread start ", threading.current_thread().name)  # 현재 실행 중인 스레드 이름 출력
        time.sleep(5)  # 5초 동안 실행을 멈춥니다 (스레드의 작업을 시뮬레이션)
        print("sub thread end ", threading.current_thread().name)  # 스레드 작업 종료 알림

# 메인 스레드의 시작을 알리는 메시지를 출력
print("main thread start")

# Worker 클래스의 첫 번째 스레드를 생성하고 실행
t1 = Worker("1")  # 이름이 "1"인 서브 스레드 생성
t1.start()        # 서브 스레드 실행 (내부적으로 run 메서드가 호출됨)

# Worker 클래스의 두 번째 스레드를 생성하고 실행
t2 = Worker("2")  # 이름이 "2"인 서브 스레드 생성
t2.start()        # 서브 스레드 실행

# join() 메서드를 호출하여 메인 스레드가 서브 스레드의 종료를 기다림
t1.join()  # t1 스레드가 종료될 때까지 메인 스레드 대기
t2.join()  # t2 스레드가 종료될 때까지 메인 스레드 대기

# 서브 스레드가 모두 종료된 후 메인 스레드의 후속 작업 수행
print("main thread post job")  # 서브 스레드 종료 후 후속 작업 알림 메시지 출력

# 메인 스레드 종료를 알리는 메시지 출력
print("main thread end")
