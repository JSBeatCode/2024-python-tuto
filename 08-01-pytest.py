import pytest

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_substract():
    assert substract(10, 5) == 5
    assert substract(0, 1) == -1
    assert substract(5, 5) == 1
    
# 5. pytest를 실행하여 테스트 확인
# 위의 테스트 코드를 작성한 후 터미널에서 pytest를 실행하면 테스트 결과가 출력됩니다.
# 모든 테스트가 성공하면 passed로 표시됩니다.
# 이렇게 pytest를 사용하면 코드가 올바르게 작동하는지 쉽게 테스트할 수 있습니다!
# 실행 명령어: pytest 08-01-pytest.py