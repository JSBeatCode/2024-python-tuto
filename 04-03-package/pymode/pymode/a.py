# a.py는 pymode 패키지에서 core 모듈과 상호작용하는 기능을 제공합니다.

from .core import CoreFunction

def func_a():
    """core 모듈의 CoreFunction을 사용하여 기능을 수행합니다."""
    data = "Data from func_a"
    result = CoreFunction(data)  # CoreFunction 호출
    return f"func_a executed: {result}"