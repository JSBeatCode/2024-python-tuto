# b.py는 pymode 패키지의 일부 기능을 제공하는 모듈입니다.

from .core import CoreClass

def func_b():
    """b.py의 기능을 수행하는 함수입니다."""
    # return "Function B executed"
    core_instance = CoreClass()
    data = "Data from func_b"
    result = core_instance.process_data(data)
    return f"func_b executed: {result}"