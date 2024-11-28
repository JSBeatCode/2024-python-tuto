"""
1. **코루틴이란?**
   - 함수 실행 도중 `yield` 키워드를 만나면 실행을 중단하고 제어권을 호출자에게 반환합니다.
   - 이후 중단된 위치에서 다시 실행을 재개할 수 있습니다.
   - 데이터 스트림 처리, 비동기 I/O 작업 등에 활용됩니다.

2. **코루틴 생성 및 초기화**:
   - `coroutine_example` 함수는 코루틴으로 동작합니다.
   - 코루틴 객체를 생성한 후에는 반드시 초기화를 위해 `next()`나 `send(None)`를 호출해야 합니다.

3. **코루틴에서 `yield` 역할**:
   - `yield`는 실행을 중단하고 제어권을 반환하며, 이후에 외부에서 값을 전달받아 실행을 재개할 수 있습니다.

4. **코루틴의 동작 순서**:
   - 처음 `next(co)`를 호출하면 함수 실행이 시작되어 `yield`에서 중단됩니다.
   - `co.send(value)`로 값을 전달하면 중단된 위치에서 실행을 재개하며 전달된 값이 `received` 변수에 저장됩니다.

5. **코루틴 종료**:
   - `co.close()`를 호출하면 코루틴을 종료합니다.
   - 종료된 코루틴에 대해 `send()`를 호출하면 `StopIteration` 예외가 발생합니다.

"""

"""
### 코루틴 주요 활용
- **데이터 생산자-소비자 패턴**:
  - 생산자와 소비자가 서로 데이터를 주고받으며 작업을 수행.
- **비동기 프로그래밍**:
  - `asyncio` 모듈과 함께 사용해 효율적인 비동기 코드를 작성 가능.
- **데이터 스트림 처리**:
  - 파일 읽기, 네트워크 패킷 처리 등에 활용.
"""

# 코루틴(Coroutine) 예제 코드
# 코루틴은 함수 내부에서 중단 및 재개가 가능한 특별한 형태의 함수입니다.
# 주로 비동기 작업이나 데이터 스트림 처리를 위해 사용됩니다.

# 코루틴 함수 정의
def coroutine_example():
    print("코루틴이 초기화되었습니다.")
    while True:
        # 외부에서 값을 받아들입니다.
        received = yield
        print(f"코루틴이 받은 값: {received}")

# 코루틴 객체 생성
co = coroutine_example()

# 코루틴 초기화 (next()를 사용하거나 send(None) 호출)
next(co)  # 코루틴을 활성화하여 실행을 시작합니다. (첫 번째 yield에서 중단됨)
# 출력: "코루틴이 초기화되었습니다."

# 코루틴에 값 전달
co.send(10)  # 코루틴 내부로 값 10을 보냅니다.
# 출력: "코루틴이 받은 값: 10"

co.send(20)  # 코루틴 내부로 값 20을 보냅니다.
# 출력: "코루틴이 받은 값: 20"

# 코루틴 종료
co.close()  # 코루틴을 종료합니다.
# 이후로는 send()를 호출하면 StopIteration 예외가 발생합니다.

print("코루틴 예제 종료")
