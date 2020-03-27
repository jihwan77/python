 # 숫자형
# 파이썬 모든 자료형
"""
int : 정수
float : 실수
complex :  복소수
bool : 불린
str : 문저열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""
# 데이타타입
str1 = "Python"
bool_v = True
str2 = 'Anaconda'
float_v = 10.0 # 10 != 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning.",
    "version": 2.0
}
tuple = (7, 8, 9) # 7, 8, 9
set = {3, 5, 7}



# 데이타타입 출력
print(type(str1), type(bool_v), type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 연산자 활용
# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x ** y (x의 y제곱) -> 2 ** 3 pow(2, 3)
"""
## 정수선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777779999999999999999999999999999999999999999
print(i)
print(i2)
print(big_int)

# 실수 출력
f = 0.9999
f2 = 3.145192
f3 = -3.0
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777777777779999999999912312312
big_int2 = 2332245823482378947239847328974239874978234
f1 = 1.234
f2 = 3.939

# +
print(">>>>>   +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
# *
print(">>>>> *")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)
print()
# 형변환
a = 3.
b = 7
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0
print(float(False)) # 0.0
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))

# 숫치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 나눈다음 몫과 나머지를 담아준다
print(x, y)
print(pow(5, 3), 5 ** 3)

# 외부모듈사용
import math
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)
