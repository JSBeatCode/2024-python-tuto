# import logging

# logging.basicConfig(level=logging.INFO)


# def hap(a,b):
#     ret = a+b
#     logging.info(f"input: {a} {b}, output={ret}")
#     return ret

# result = hap(3,4)

print('-------------------------------')
# 파일에 로깅하기
import logging  # logging 모듈을 임포트합니다.

# 1. 로그 설정
# 로그 메시지를 파일에 기록하기 위해 기본 설정을 구성합니다.
logging.basicConfig(
    filename='app.log',  # 로그 메시지가 기록될 파일 이름을 지정합니다.
    level=logging.INFO,  # 로그의 수준을 INFO로 설정합니다. (DEBUG < INFO < WARNING < ERROR < CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # 로그 메시지의 형식을 지정합니다.
    encoding='utf-8'  # 로그 파일의 인코딩을 utf-8로 설정합니다.
    # %(asctime)s: 로그 기록 시간
    # %(levelname)s: 로그의 심각도 수준
    # %(message)s: 로그 메시지 내용
)

# 2. 로그 메시지 기록
logging.info("이것은 INFO 메시지입니다.")  # 정보 메시지를 기록합니다.
logging.warning("이것은 WARNING 메시지입니다.")  # 경고 메시지를 기록합니다.
logging.error("이것은 ERROR 메시지입니다.")  # 오류 메시지를 기록합니다.

# 3. 프로그램 실행 시 app.log 파일이 생성되고 위의 로그 메시지가 해당 파일에 기록됩니다.
