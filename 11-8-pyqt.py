import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from multiprocessing import Process, Queue
import multiprocessing as mp
import datetime
import time

# 생산자 프로세스 함수 (현재 시간을 문자열로 큐에 넣는 역할)
def producer(q):
    proc = mp.current_process()  # 현재 프로세스 정보를 가져옴
    print(proc.name)  # 프로세스의 이름 출력

    while True:
        now = datetime.datetime.now()  # 현재 시간을 가져옴
        data = str(now)  # 현재 시간을 문자열로 변환
        q.put(data)  # 큐에 현재 시간 데이터를 넣음
        time.sleep(1)  # 1초마다 데이터를 큐에 넣음


# 소비자 클래스 (QThread를 상속받아 큐에서 데이터를 가져와 처리하는 역할)
class Consumer(QThread):
    poped = pyqtSignal(str)  # pyqtSignal을 사용하여 데이터를 전달

    def __init__(self, q):
        super().__init__()  # 부모 클래스 QThread의 초기화
        self.q = q  # 큐를 클래스 변수로 저장

    def run(self):
        while True:
            if not self.q.empty():  # 큐에 데이터가 있을 때만
                data = self.q.get()  # 큐에서 데이터를 꺼냄
                self.poped.emit(data)  # 데이터를 poped 시그널로 전달


# 메인 윈도우 클래스 (QMainWindow를 상속받아 UI와 기능을 정의)
class MyWindow(QMainWindow):
    def __init__(self, q):
        super().__init__()
        self.setGeometry(200, 200, 300, 200)  # 윈도우 크기 및 위치 설정

        # 소비자 클래스 객체 생성 (큐를 전달)
        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.print_data)  # 시그널 연결: 소비자가 데이터를 처리하면 print_data 메서드 호출
        self.consumer.start()  # 소비자 스레드를 시작

    # 데이터를 출력하는 메서드
    @pyqtSlot(str)  # 시그널을 받을 슬롯으로 지정
    def print_data(self, data):
        self.statusBar().showMessage(data)  # 상태 표시줄에 데이터를 출력


if __name__ == "__main__":
    q = Queue()  # 큐 객체 생성

    # 생산자 프로세스 생성 (큐를 인자로 넘김)
    p = Process(name="producer", target=producer, args=(q, ), daemon=True)
    p.start()  # 생산자 프로세스 시작

    # 메인 애플리케이션 실행
    app = QApplication(sys.argv)  # QApplication 객체 생성
    mywindow = MyWindow(q)  # MyWindow 객체 생성 (큐를 인자로 넘김)
    mywindow.show()  # 윈도우 표시
    app.exec_()  # 애플리케이션 실행 (이벤트 루프 시작)
