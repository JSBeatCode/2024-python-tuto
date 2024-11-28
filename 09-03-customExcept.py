# 사용자 정의 예외 클래스 정의
class NegativeNumberError(Exception):
    """음수를 입력했을 때 발생하는 사용자 정의 예외"""
    def __init__(self, value):
        self.value = value
        self.message = f"입력한 값 {value}은(는) 음수입니다. 양수를 입력해 주세요."
        super().__init__(self.message)  # 부모 클래스의 __init__ 호출

# 숫자 입력 및 검사 함수
def check_positive_number():
    try:
        num = int(input("양수를 입력하세요: "))  # 사용자로부터 숫자 입력받기
        if num < 0:
            raise NegativeNumberError(num)  # num이 음수이면 사용자 정의 예외 발생
        print(f"입력한 숫자는 {num}입니다.")
    except NegativeNumberError as e:
        # 사용자 정의 예외가 발생했을 때 실행되는 코드 블록
        print(f"오류: {e}")  # 예외 메시지를 출력합니다.
    except ValueError:
        # 입력값이 정수가 아닐 때 발생하는 ValueError 처리
        print("유효한 숫자를 입력해 주세요.")
    finally:
        # 예외 발생 여부와 상관없이 항상 실행되는 블록
        print("프로그램이 종료되었습니다.")

# 함수 호출
check_positive_number()
