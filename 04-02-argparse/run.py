# 만약 어떤 옵션에 따라서 파이썬 스크립트가 다르게 동작하도록 해주려면 명령행을 통해 이러한 인자를 받아야합니다
# ./run.py -d 1 -f

import argparse  # argparse 모듈을 가져옵니다. 명령줄 인자를 파싱하기 위해 사용됩니다.

# ArgumentParser 객체를 생성합니다. 이 객체는 명령줄 옵션과 인자를 처리합니다.
parser = argparse.ArgumentParser()

# 명령줄 인자 '-d' 또는 '--decimal'을 추가합니다.
# dest="decimal": 인자의 값을 'args' 객체의 'decimal' 속성에 저장합니다.
# action="store": 인자의 값을 그대로 저장합니다.
parser.add_argument("-d", "--decimal", dest="decimal", action="store")

# 명령줄 인자 '-f' 또는 '--fast'를 추가합니다.
# dest="fast": 인자의 값을 'args' 객체의 'fast' 속성에 저장합니다.
# action="store_true": 인자가 제공되면 'True'로 저장하고, 제공되지 않으면 'False'로 설정합니다.
parser.add_argument("-f", "--fast", dest="fast", action="store_true")

# 명령줄 인자를 파싱하고 'args' 객체에 저장합니다.
args = parser.parse_args()

# args 객체의 'decimal' 속성 값을 출력합니다. (사용자가 제공한 인자 값)
print(args.decimal)

# args 객체의 'fast' 속성 값을 출력합니다. (사용자가 '-f' 또는 '--fast'를 제공했는지 여부)
print(args.fast)

# 실행명령어
# & C:/Users/jsd/AppData/Local/Programs/Python/Python311-32/python.exe c:/Users/jsd/Documents/programming/python-tuto-2024/04-02-argparse/run.py -d 1 -f
