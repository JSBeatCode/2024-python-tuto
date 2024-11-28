# core.py는 pymode 패키지의 핵심 기능을 제공하는 모듈입니다.

def CoreFunction(data):
    """핵심 기능을 수행하는 함수입니다."""
    return f"Core function received: {data}"

# 핵심 기능을 제공하는 클래스 정의
class CoreClass:
    """핵심 기능을 담당하는 클래스입니다."""

    def __init__(self):
        self.message = "CoreClass initialized"

    def process_data(self, data):
        """데이터를 처리하는 메서드입니다."""
        return f"CoreClass processed: {data}"
