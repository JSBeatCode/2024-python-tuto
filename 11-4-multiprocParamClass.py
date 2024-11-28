import multiprocessing as mp  # 멀티프로세싱을 위한 모듈 임포트


# Worker 클래스 정의
class Worker:
    """
    작업을 수행하는 Worker 클래스입니다.
    멀티프로세싱에서 실행할 작업 메서드를 포함합니다.
    """
    def __init__(self):
        # 초기화 메서드. 현재는 특별한 초기화 작업을 수행하지 않습니다.
        pass

    def run(self, value):
        """
        작업을 수행하는 메서드.
        현재 프로세스 이름과 전달받은 값을 출력합니다.
        """
        pname = mp.current_process().name  # 현재 실행 중인 프로세스 이름 가져오기
        print(pname, value)  # 프로세스 이름과 전달받은 값을 출력


# 메인 프로세스에서 실행되는 코드
if __name__ == "__main__":
    # Worker 클래스의 인스턴스 생성
    w = Worker()

    # 새로운 프로세스를 생성
    # name: 프로세스의 이름을 지정
    # target: 실행할 메서드를 지정 (Worker 클래스의 run 메서드)
    # args: 실행할 메서드에 전달할 인수를 튜플로 지정
    p = mp.Process(name="Sub Process", target=w.run, args=("hello class",))

    p.start()  # 서브 프로세스 시작 (run 메서드 실행)

    p.join()  # 서브 프로세스가 종료될 때까지 대기

    # 메인 프로세스에서 메시지 출력
    print("Main Process")
