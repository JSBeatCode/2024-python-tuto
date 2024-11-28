import multiprocessing as mp  # 멀티프로세싱을 위한 모듈 임포트


# 작업 함수 정의
def work(value):
    """
    프로세스에서 실행될 작업 함수.
    현재 프로세스의 이름과 전달받은 값을 출력합니다.
    """
    pname = mp.current_process().name  # 현재 실행 중인 프로세스의 이름 가져오기
    print(pname, value)  # 프로세스 이름과 전달된 값 출력


# 메인 프로세스에서 실행되는 코드
if __name__ == "__main__":
    # mp.Process를 사용하여 새로운 서브 프로세스 생성
    # name: 생성할 프로세스의 이름
    # target: 실행할 함수
    # args: 실행할 함수에 전달할 인수 (튜플 형태로 전달)
    p = mp.Process(name="Sub Process", target=work, args=("hello",))

    p.start()  # 서브 프로세스 시작 (work 함수 실행)

    p.join()  # 서브 프로세스가 종료될 때까지 대기

    print("Main Process")  # 메인 프로세스에서 메시지 출력
