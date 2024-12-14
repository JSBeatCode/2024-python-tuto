"""
이 예제에서는 두 프로세스 간에 데이터를 주고받기 위해 Queue를 사용합니다. 
queue.put()으로 데이터를 넣고, queue.get()으로 데이터를 꺼내어 처리하는 
방식으로 두 프로세스가 자원을 안전하게 주고받습니다.
"""

import multiprocessing as mp
import time

# 자원을 처리할 함수
def process_data(queue_in, queue_out):
    # 큐에서 데이터를 가져옵니다.
    data = queue_in.get()
    print(f"{mp.current_process().name} - 받은 데이터: {data}")
    
    # 데이터를 처리 (예: 데이터를 두 배로 만들기)
    result = data * 2
    time.sleep(1)  # 데이터를 처리하는데 시간이 걸리는 상황을 시뮬레이션
    
    # 처리한 결과를 다른 큐에 넣어 전달
    print(f"{mp.current_process().name} - 처리 결과: {result}")
    queue_out.put(result)

if __name__ == "__main__":
    # 두 개의 큐를 생성합니다.
    queue1 = mp.Queue()  # 첫 번째 큐: 데이터를 전달
    queue2 = mp.Queue()  # 두 번째 큐: 처리된 결과를 전달
    
    # 자원 전달을 위한 프로세스를 생성
    p1 = mp.Process(target=process_data, args=(queue1, queue2), name="Process-1")
    p2 = mp.Process(target=process_data, args=(queue2, queue1), name="Process-2")
    
    # 프로세스 시작
    p1.start()
    p2.start()
    
    # 첫 번째 큐에 데이터를 넣어 두 번째 프로세스에게 전달
    queue1.put(5)  # 5라는 데이터를 첫 번째 큐에 넣음
    
    # 두 프로세스가 종료될 때까지 기다립니다.
    p1.join()
    p2.join()
    
    # 최종 결과를 출력합니다.
    while not queue1.empty():
        print(f"최종 결과: {queue1.get()}")
