import multiprocessing as mp
import time

class Work:
    def __init__(self):
        # Work 클래스 초기화. 현재는 특별한 동작을 하지 않음.
        pass
    
    def run(self):
        # 서브 프로세스에서 실행할 메서드
        # 무한 루프를 돌며 "sub process is running"을 출력하고, 1초 간격으로 대기
        while True:
            print("sub process is running")
            time.sleep(1)

if __name__ == "__main__":
    # Work 클래스의 인스턴스를 생성
    w = Work()
    
    # Work 클래스의 run 메서드를 서브 프로세스로 실행
    # target에 메서드 참조를 전달하고, 이름은 "SubProcess"로 설정
    p = mp.Process(target=w.run, name="SubProcess")
    
    # 프로세스가 시작되기 전 상태 확인 (False 예상)
    print("Status: ", p.is_alive())
    
    # 서브 프로세스 시작
    p.start()
    
    # 프로세스가 실행 중인지 상태 확인 (True 예상)
    print("Status: ", p.is_alive())
    
    # 메인 프로세스가 5초 동안 대기 (서브 프로세스가 실행되는 동안)
    time.sleep(5)
    
    # 서브 프로세스를 강제 종료 (kill)
    p.kill()
    
    # 프로세스 종료 후 상태 확인 (False 예상하나, p.kill() 호출 직후 is_alive()를 호출할 경우, 서브 프로세스가 종료 처리 중일 수 있어 일시적으로 True를 반환할 가능성이 있습니다.)
    print("Status: ", p.is_alive())
    
    # 서브 프로세스의 종료를 기다림 (join)
    p.join()
    
    # 최종적으로 프로세스가 종료되었는지 상태 확인 (False 예상)
    print("Status: ", p.is_alive())
