# 아이스크림 이름 리스트와 가격 리스트
name = ['merona', 'gugucon']  # 아이스크림 이름들
price = [500, 1000]           # 아이스크림 가격들

# 두 리스트를 합쳐 딕셔너리를 생성
# zip() 함수는 name과 price를 순서대로 묶어 튜플로 반환
# 이를 딕셔너리로 변환
icecream = {k: v for k, v in zip(name, price)}
print(icecream)  
# 출력: {'merona': 500, 'gugucon': 1000}

# 가격을 2배로 한 딕셔너리 생성
# zip()으로 묶은 후 딕셔너리 컴프리헨션으로 가격에 2를 곱함
icecream2 = {k: v * 2 for k, v in zip(name, price)}
print(icecream2)  
# 출력: {'merona': 1000, 'gugucon': 2000}

# 이름과 가격 리스트를 확장
name1 = ['merona', 'gugucon', 'dfes']  # 아이스크림 이름들
price1 = [500, 1000, 600]             # 아이스크림 가격들

# 가격이 1000 미만인 아이스크림만 딕셔너리에 저장
# 조건식 `if v < 1000`을 사용하여 가격 필터링
icecream3 = {k: v for k, v in zip(name1, price1) if v < 1000}
print(icecream3)  
# 출력: {'merona': 500, 'dfes': 600}
