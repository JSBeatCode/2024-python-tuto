import multiprocessing as mp  # 멀티프로세싱 기능을 제공하는 모듈
import time  # 시간 지연 처리를 위한 모듈

# 서브 프로세스에서 실행할 작업 함수 정의
def work():
    while True:  # 무한 루프를 실행
        print("sub process is running")  # 서브 프로세스가 실행 중임을 출력
        time.sleep(1)  # 1초 대기

# 메인 실행 블록
if __name__ == "__main__":
    # 서브 프로세스를 생성합니다.
    p = mp.Process(
        target=work,  # 실행할 함수(work)를 지정
        name="SubProcess"  # 서브 프로세스의 이름을 지정
    )

    # 서브 프로세스가 실행 중인지 확인 (현재는 시작 전이므로 False)
    print("Status: ", p.is_alive())

    # 서브 프로세스를 시작합니다.
    p.start()

    # 서브 프로세스가 실행 중인지 확인 (시작되었으므로 True)
    print("Status: ", p.is_alive())

    # 2초 동안 메인 프로세스가 대기
    time.sleep(2)

    # 서브 프로세스를 강제로 종료합니다.
    p.kill()

    # 서브 프로세스가 실행 중인지 확인 (종료되었으므로 False, 그러나 p.kill() 호출 직후 상태 확인 했으므로 -> 종료되지 않은 상태)
    print("Status: ", p.is_alive())
    # 여기서 부턴 종료된 상태일 것임 (p.kill()은 강제 종료 명령이며, 처리 속도에 따라 is_alive()의 상태가 잠시 동안 True로 남아 있을 수 있습니다.)
    
    # 서브 프로세스의 종료를 기다립니다. (리소스 정리 포함)
    p.join()

    # 서브 프로세스가 실행 중인지 최종 확인 (False)
    print("Status: ", p.is_alive())

