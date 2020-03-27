# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

import sys
print(sys.argv)

# 강제 종료
# sys.exit()

# 파이썬 패키지 위치
print(sys.path)

# pickle : 객체 파일 읽기, 쓰기
import pickle # 파이썬 데이타 타입을 파일에 쓸수 있다

# 쓰기
f = open('test.obj', 'wb') # write 바이너리
obj = {1: 'Python', 2: 'Study', 3: 'Basic'}
pickle.dump(obj, f)
f.close()

# 읽기
f = open('test.obj', 'rb') # read 바이너리
data = pickle.load(f)
print(data, type(data)) # {1: 'Python', 2: 'Study', 3: 'Basic'} <class 'dict'>
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

import os
print(os.environ)
print(os.environ["USERNAME"])

# 현재 경로
print(os.getcwd())

# time : 시간 관련 처리
import time
print(time.time()) # 1582367868.6343458
# 형태 변환
print(time.localtime(time.time())) # time.struct_time(tm_year=2020, tm_mon=2, tm_mday=22, tm_hour=19, tm_min=37, tm_sec=48, tm_wday=5, tm_yday=53, tm_isdst=0)
# 간단 표현
print(time.ctime()) # Sat Feb 22 19:37:48 2020
# 형식 표현
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 시간 간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import random
print(random.random()) # 0~1 실수
print(random.randint(1, 45)) # 1~45
print(random.randrange(1, 45)) # 1~44
#  섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)
# 무작위 선택
c = random.choice(d)
print(c)

# webbrowser : 본인 OS의 웹 브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")