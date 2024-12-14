# 멀티프로세싱(Multiprocessing) 예제 코드
# 멀티프로세싱을 사용하면 여러 프로세스를 생성하여 병렬로 작업을 수행할 수 있습니다.
# 이는 CPU를 더 효율적으로 활용하고, I/O가 많은 작업을 병렬 처리하는 데 유용합니다.

import multiprocessing  # 멀티프로세싱을 위한 모듈 임포트
import time


# 각 프로세스에서 실행할 작업 함수 정의
def worker_function(task_id):
    """
    각 프로세스에서 수행할 작업 함수.
    task_id: 작업 고유 ID
    """
    print(f"프로세스 {task_id} 시작")  # 작업 시작 메시지 출력
    time.sleep(2)  # 작업을 시뮬레이션하기 위해 2초 대기
    print(f"프로세스 {task_id} 완료")  # 작업 완료 메시지 출력


# 파이썬에서 멀티프로세싱을 사용할 때는 반드시 `if __name__ == "__main__":` 블록 안에서 작업을 정의해야 합니다.
# 이는 Windows와 같은 플랫폼에서 새로운 프로세스가 잘못 실행되지 않도록 방지합니다.
if __name__ == "__main__":
    # 메인 프로세스 실행 확인
    print("메인 프로세스 시작")

    # 프로세스를 저장할 리스트
    processes = []

    # 4개의 프로세스 생성 및 시작
    for i in range(4):
        # Process 객체 생성
        # `target`에 실행할 함수를 지정하고, `args`에 함수에 전달할 인수를 지정합니다.
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)  # 생성한 프로세스를 리스트에 저장
        process.start()  # 프로세스 실행

    # 모든 프로세스가 종료될 때까지 대기
    for process in processes:
        # `process.join()`은 해당 프로세스가 작업을 완료할 때까지 메인 프로세스가 대기하도록 합니다.
        process.join()

    # 모든 작업 완료 후 출력
    print("모든 작업 완료")
