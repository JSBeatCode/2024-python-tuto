from datetime import datetime

now = datetime.now()

# 각 서식 코드의 예제를 출력합니다.
print("요일의 약칭:", now.strftime("%a"))
print("요일의 전체 이름:", now.strftime("%A"))
print("요일 (0: 일요일, 6: 토요일):", now.strftime("%w"))
print("0을 채운 날짜 (01-31):", now.strftime("%d"))
print("월의 약칭:", now.strftime("%b"))
print("월의 전체 이름:", now.strftime("%B"))
print("0을 채운 월 (01-12):", now.strftime("%m"))
print("세기 없이 연도 (00-99):", now.strftime("%y"))
print("세기를 포함한 연도:", now.strftime("%Y"))
print("24시간 형식의 시간 (00-23):", now.strftime("%H"))
print("12시간 형식의 시간 (01-12):", now.strftime("%I"))
print("AM 또는 PM:", now.strftime("%p"))
print("0을 채운 분 (00-59):", now.strftime("%M"))
print("0을 채운 초 (00-59):", now.strftime("%S"))
print("마이크로초 (6자리):", now.strftime("%f"))
print("UTC 오프셋:", now.strftime("%z"))
print("시간대 이름:", now.strftime("%Z"))
print("0을 채운 연중 일자 (001-366):", now.strftime("%j"))
print("0을 채운 연중 주차 (일요일 기준):", now.strftime("%U"))
print("0을 채운 연중 주차 (월요일 기준):", now.strftime("%W"))
print("현지 날짜와 시간:", now.strftime("%c"))
print("현지 날짜:", now.strftime("%x"))
print("현지 시간:", now.strftime("%X"))
print("% 문자 자체:", now.strftime("%%"))


print('-------------------------------------')

from datetime import date  # date 클래스를 임포트하여 날짜 관련 기능을 사용

# 현재 날짜를 가져옵니다.
now = date.today()
print(now)  # 현재 날짜를 출력합니다.

# 날짜 형식을 포맷하여 보기 좋게 출력합니다.
# %m: 월(숫자), %d: 일, %y: 연도(두 자리), %b: 월(약어), %Y: 연도(네 자리)
# %A: 요일 이름, %B: 월 이름
tim = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B")
print(tim)  # 포맷된 날짜 정보를 출력합니다.

# 특정 날짜(1988년 11월 28일, 예: 생일)를 정의합니다.
birthday = date(1988, 11, 28)
# 현재 날짜와 생일 사이의 일 수 차이를 계산합니다.
age = now - birthday
print(age.days)  # 총 일 수를 출력합니다.
print(round(age.days / 365))  # 대략적인 나이를 연 단위로 계산하여 출력합니다.

print('-------------------------------------')


now1 = datetime.now()
print(now1)

now2 = datetime(2024, 11, 11, 12, 30, 22, 908778)
print(now2)

today = datetime(
    year = now1.year,
    month = now1.month,
    day = now1.day,
    hour = now1.hour,
    minute = now1.minute,
    second = now1.second,
)

print(today)

print('-------------------------------------')
# timedelta 객체는 두 날짜나 시간의 차이인 기간을 나타냅니다.
from datetime import datetime, timedelta

# 현재 날짜와 시간 가져오기
now = datetime.now()

# timedelta로 날짜 더하기 (3일 후)
three_days_later = now + timedelta(days=3)
print("3일 후:", three_days_later)

# timedelta로 날짜 빼기 (5일 전)
five_days_ago = now - timedelta(days=5)
print("5일 전:", five_days_ago)

# 시간 더하기 (2시간 후)
two_hours_later = now + timedelta(hours=2)
print("2시간 후:", two_hours_later)

# 10분 빼기
ten_minutes_ago = now - timedelta(minutes=10)
print("10분 전:", ten_minutes_ago)

# 날짜 차이 계산
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
difference = date2 - date1  # 두 날짜 간의 차이를 구함
print("2024년 1월 1일부터 12월 31일까지의 일수:", difference.days)

# 두 날짜 간의 차이를 시, 분, 초 단위로 계산
print("두 날짜 간의 차이 (시, 분, 초):", difference)
print("시:", difference.seconds // 3600)
print("분:", (difference.seconds % 3600) // 60)
print("초:", (difference.seconds % 3600) % 60)

print('----------------------------------------------')

# 타임존변경
# pip install pytz

from datetime import datetime  # datetime 모듈에서 datetime 클래스를 임포트
import pytz  # pytz 모듈을 임포트 (시간대 처리용)

# 예시로 사용할 'datetime' 객체 생성 (2021년 1월 1일, 00:00:00)
# tzinfo=pytz.UTC로 UTC 시간대 정보를 추가
dt_utc = datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)  # UTC 시간대 설정

# 'Asia/Seoul' 시간대 객체 생성
seoul_timezone = pytz.timezone('Asia/Seoul')

# UTC 시간에서 'Asia/Seoul' 시간대로 변환
dt_seoul = dt_utc.astimezone(seoul_timezone)  # astimezone()을 사용하여 시간대 변환

# 'Asia/Seoul' 시간대 정보를 제거하여 naive datetime 객체로 변환
# naive datetime은 시간대 정보가 없는 datetime 객체
# replace(tzinfo=None)를 사용하여 datetime 객체에서 시간대 정보를 제거하여 naive datetime 객체로 만듭니다. 
# 이는 시간대 정보 없이 순수한 날짜와 시간만 포함하는 객체입니다.
dt_naive = dt_seoul.replace(tzinfo=None)  # tzinfo=None을 설정하여 시간대 정보 제거

# 결과 출력
print("UTC 시간:", dt_utc)  # UTC 시간 출력
print("서울 시간:", dt_seoul)  # 서울 시간 출력
print("Naive 시간:", dt_naive)  # 시간대 정보가 없는 naive datetime 출력
