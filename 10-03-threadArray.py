import threading  # 스레드 생성을 위해 threading 모듈을 임포트
import time       # 시간 지연을 위해 time 모듈을 임포트

# Worker 클래스 정의 - threading.Thread를 상속받아 사용자 정의 스레드 생성
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()  # 부모 클래스 초기화 메서드 호출
        self.name = name  # 스레드 이름 설정
    
    def run(self):
        # 현재 실행 중인 스레드의 이름 출력 (작업 시작 알림)
        print("sub thread start ", threading.current_thread().name)
        time.sleep(5)  # 5초 동안 대기 (스레드 작업 시뮬레이션)
        # 현재 실행 중인 스레드의 이름 출력 (작업 종료 알림)
        print("sub thread end ", threading.current_thread().name)
        
# 메인 스레드 시작 알림 메시지 출력
print("main thread start")

# 서브 스레드를 저장할 리스트 생성
thread_arr = []

# 3개의 서브 스레드 생성 및 실행
for i in range(3):  # i는 0, 1, 2 값을 가짐
    thread = Worker(i)  # 이름이 i인 Worker 스레드 생성
    thread.start()  # 스레드 실행 (내부적으로 run 메서드 호출)
    thread_arr.append(thread)  # 실행된 스레드를 리스트에 추가
    
# 모든 서브 스레드가 종료될 때까지 대기
for one_thread in thread_arr:
    one_thread.join()  # 각 스레드가 종료될 때까지 메인 스레드 대기
    
# 모든 서브 스레드 종료 후 메인 스레드 후속 작업 알림 메시지 출력
print("main thread post job")

# 메인 스레드 종료 알림 메시지 출력
print("main thread end")
