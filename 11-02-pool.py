# 멀티프로세싱에서 Pool을 사용한 예제 코드
# Pool은 여러 프로세스를 생성하고 관리하여 병렬로 작업을 처리할 수 있도록 도와주는 유용한 기능입니다.

import multiprocessing  # 멀티프로세싱을 위한 모듈 임포트
import time


# 각 프로세스에서 실행할 작업 함수 정의
def worker_function(task_id):
    """
    각 프로세스에서 수행할 작업 함수.
    task_id: 작업 고유 ID
    """
    print(f"작업 {task_id} 시작")  # 작업 시작 메시지 출력
    time.sleep(2)  # 작업을 시뮬레이션하기 위해 2초 대기
    result = f"작업 {task_id} 완료"  # 결과 메시지 생성
    return result


# 메인 프로세스에서 Pool을 사용하여 작업 처리
if __name__ == "__main__":
    print("메인 프로세스 시작")  # 메인 프로세스 시작 메시지

    # 작업 ID 리스트 (예: 0부터 9까지 10개의 작업)
    tasks = list(range(10))

    # Pool 객체 생성 (프로세스 수: 4)
    # `multiprocessing.Pool(processes=N)`에서 N은 동시에 실행할 프로세스 수를 의미합니다.
    with multiprocessing.Pool(processes=4) as pool:
        # Pool의 map 메서드를 사용하여 병렬 작업 실행
        # map은 작업 함수와 작업 리스트를 받아 각 작업을 병렬로 처리합니다.
        results = pool.map(worker_function, tasks)

    # 모든 작업 완료 후 결과 출력
    print("모든 작업 완료")
    print("결과:", results)
