# 제너레이터 
# iterator객체의 한 종류 (next함수호출)
# 만드는 방법 : 제너레이터 함수(function) 제너레이터 표현식(expression)
def gen_num():  # 제너레이터 함수정의
    print('first number')
    yield 1 # yield가 하나라도 들어가면 제너레이터가 됩니다.
    print('second number')
    yield 2
    print('third number')
    yield 3

# 제너레이터 함수를 호출해도 실행하지 않고 제너레이터객체를 만들어 변수에 담는다.
gen = gen_num()

# next 함수를 호출하면 첫번째 yield를 만날때 까지 수행하고 멈춘다
print(next(gen)) # 첫번째 yield
print(next(gen)) # 두번째 yield
print(next(gen)) # 세번째 yield
# print(next(gen)) # StopIteration 예외발생

# next 함수가 호출될 때까지 미루는 특성을 lazy evaluation

def gen_for():
    for i in [1, 2, 3]:
        yield i

g = gen_for()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
# print(next(g)) # StopIteration 예외발생

# 제너레이터가 갖는 장점
import sys
def pows(s):
    r = []
    for i in s:
        r.append(i ** 2)
    return r
# 미리 st에 값을 미리 전부 만든다 (메모리 호율이 좋지 않다)
st = pows(range(1, 1000))
# for i in st:
#     print(i, end=' ') # 1 4 9 16 25 36 49 64 81
print('getsizeof=', sys.getsizeof(st)) #getsizeof= 9016
def gpows(s):
    for i in s:
        yield i ** 2
# 필요할때 만든다
st = gpows(range(1, 1000))
# st는 iterator객체 이면서 iterable객체이므로 for문에 올수 있다
# for i in st:
#     print(i, end=' ') # 1 4 9 16 25 36 49 64 81
print('getsizeof=', sys.getsizeof(st)) #getsizeof= 112

# lazy evaluation는 필요 할 때 만드는 연산
# map 이나 filter도 제너레이터 함수

# yield from
def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    for i in ns:
        yield i
g = get_nums()
print(next(g))
print(next(g))

def get_nums_from():
    ns = [0, 1, 0, 1, 0, 1]
    yield from ns
g = get_nums_from()
print(next(g))
print(next(g))