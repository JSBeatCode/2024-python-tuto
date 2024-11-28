# 만약 어떤 옵션에 따라서 파이썬 스크립트가 다르게 동작하도록 해주려면 명령행을 통해 이러한 인자를 받아야합니다
# ./run.py -d 1 -f

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")

parser.add_argument("-f", "--fast", dest="fast", action="store_true")

args = parser.parse_args()

print(args.decimal)
print(args.fast)


print('-----------------------------------------------')

import argparse

parser1 = argparse.ArgumentParser()
parser1.add_argument(dest="width", action="store")
parser1.add_argument(dest="height", action="store")
parser1.add_argument("--frames", dest="frames", action="store")
parser1.add_argument("--qp", dest="qp", action="store")
parser1.add_argument("--configure", dest="configure", action="store")


args1 = parser1.parse_args(["64", "56", "--frames", "60", "--qp", "1", "--configure", "AI"])

print(
    args1.width, 
    args1.height, 
    args1.frames,
    args1.qp,
    args1.configure
    )