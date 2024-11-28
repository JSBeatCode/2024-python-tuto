# 예외 처리 예제 코드

try:
    # 예외가 발생할 수 있는 코드 블록
    num1 = int(input("첫 번째 숫자를 입력하세요: "))  # 사용자로부터 숫자를 입력받아 정수로 변환
    num2 = int(input("두 번째 숫자를 입력하세요: "))  # 두 번째 숫자도 정수로 변환
    result = num1 / num2  # 두 숫자를 나누기
except ValueError:
    # ValueError 예외 처리: 입력값이 정수가 아닐 경우 실행됩니다.
    print("숫자가 아닌 값을 입력하셨습니다. 정수를 입력해 주세요.")
except ZeroDivisionError:
    # ZeroDivisionError 예외 처리: 0으로 나누려고 할 때 실행됩니다.
    print("0으로 나눌 수 없습니다. 두 번째 숫자는 0이 아니어야 합니다.")
else:
    # 예외가 발생하지 않았을 경우 실행되는 블록
    print(f"결과: {result}")  # 나누기 결과를 출력합니다.
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 블록
    print("프로그램이 종료되었습니다.")  # 프로그램 종료 메시지를 출력합니다.
