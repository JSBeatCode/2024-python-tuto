
import timeit  # 코드 실행 시간을 측정하기 위해 timeit 모듈을 임포트합니다.

# 측정할 실제 함수
def example_function():
    # 리스트 내포를 사용하여 0부터 999까지의 숫자의 제곱 값을 계산합니다.
    result = [x ** 2 for x in range(1000)]
    return result  # 계산된 리스트를 반환합니다.

# timeit.timeit() 함수를 사용해 example_function의 실행 시간을 측정합니다.
# 첫 번째 인자로 실행할 함수를 전달합니다.
# number=1000은 함수가 1000번 실행되도록 설정합니다.
execution_time = timeit.timeit(example_function, number=1000)

# 측정된 총 실행 시간을 출력합니다. 실행 시간은 초 단위로 반환됩니다.
print(f"실행 시간: {execution_time}초")

print('-------------------------------------')

# 코드를 실행하면 doctest가 문서화된 예제와 실제 함수 결과를 비교합니다.
# 모든 테스트가 성공하면 아무 메시지도 출력되지 않습니다.
# 테스트가 실패하면 어디에서 오류가 발생했는지에 대한 정보가 출력됩니다.

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """ 
    # 아래를 return 하면 doctest가 오류를 잡는다.
    # return sum(values) / len(values.d)
    return sum(values) / len(values)

import doctest
doctest.testmod()

print('-------------------------------------')

import unittest  # 파이썬 표준 라이브러리인 unittest 모듈을 임포트합니다. 이 모듈은 단위 테스트를 작성하고 실행하는 데 사용됩니다.

# TestStatisticalFunctions 클래스는 unittest.TestCase를 상속받아 정의됩니다.
# 이 클래스는 통계 함수를 테스트하는 메서드를 포함합니다.
class TestStatisticalFunctions(unittest.TestCase):
    
    # testAverage라는 이름의 메서드를 정의합니다.
    # 이 메서드는 average 함수의 동작을 테스트합니다.
    def testAverage(self):
        # average 함수의 결과를 출력합니다 (테스트 확인을 위해).
        print(average([20, 30, 70]))
        # average 함수가 주어진 리스트 [20, 30, 70]에 대해 40.0을 반환하는지 확인합니다.
        self.assertEqual(average([20, 30, 70]), 40.0)
        
        # average 함수의 결과를 반올림하여 출력합니다.
        print(round(average([1, 5, 7]), 1))
        # average 함수가 [1, 5, 7]에 대해 4.3을 반환하는지 확인합니다 (소수 첫째 자리까지 반올림).
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        
        # with self.assertRaises: 특정 예외가 발생하는지 확인합니다. 예외가 발생하지 않으면 테스트가 실패합니다.
        # 빈 리스트를 전달했을 때 ZeroDivisionError가 발생하는지 확인합니다.
        with self.assertRaises(ZeroDivisionError):
            average([])
        
        # 여러 개의 개별 숫자를 인자로 전달했을 때 TypeError가 발생하는지 확인합니다.
        with self.assertRaises(TypeError):
            average(20, 30, 70)

# unittest.main()을 호출하여 테스트를 실행합니다.
# 이 코드는 모듈이 직접 실행될 때만 작동합니다.
unittest.main()
