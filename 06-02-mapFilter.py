# map 예제: 리스트의 각 숫자에 2를 곱하기
# 주어진 리스트의 각 요소에 2를 곱하는 함수를 map으로 적용

numbers = [1, 2, 3, 4, 5]  # 숫자 리스트

# 함수 정의: 숫자에 2를 곱하는 함수
def multiply_by_two(x):
    return x * 2  # 입력된 값 x에 2를 곱해서 반환

# map()을 사용하여 multiply_by_two 함수 적용
# map은 주어진 함수(multiply_by_two)를 numbers 리스트의 각 요소에 적용하고, 그 결과를 반환
doubled_numbers = map(multiply_by_two, numbers)

# 결과는 map 객체로 반환되므로 list()로 변환하여 출력
print("각 숫자에 2를 곱한 값들:", list(doubled_numbers))  # [2, 4, 6, 8, 10]

print('-----------------------------------------')

# filter 예제: 짝수만 필터링하기
# 주어진 리스트에서 짝수만 필터링하는 함수

def is_even(x):
    return x % 2 == 0  # 숫자가 짝수일 때 True 반환

# filter()를 사용하여 is_even 함수가 True를 반환하는 값들만 필터링
# filter는 주어진 함수(is_even)를 numbers 리스트의 각 요소에 적용하고, True인 값들만 반환
even_numbers = filter(is_even, numbers)

# filter() 결과도 마찬가지로 리스트로 변환하여 출력
print("리스트에서 짝수만 필터링:", list(even_numbers))  # [2, 4]
