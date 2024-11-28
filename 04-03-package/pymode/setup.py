# setup.py는 패키지를 설치할 때 사용되는 설정 파일입니다.
from setuptools import setup, find_packages

setup(
    name="pymode",  # 패키지 이름
    version="0.1",  # 버전 번호
    packages=find_packages(),  # 모든 서브 패키지를 자동으로 찾습니다.
    description="A sample Python package with interconnected modules",
    author="Your Name",  # 작성자 이름
    author_email="your_email@example.com",  # 작성자 이메일
)