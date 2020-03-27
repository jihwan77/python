# 제너레이터 
# iterator객체의 한 종류 (next함수호출)
# 제너레이터 표현식(expression)
# 함수 -> 람다식
# 함수(제너레이터) -> 제너레이터 표현식
def show_all(s):
    for i in s:
        print(i, end=' ')
st = [2 * i for i in range(1, 10)] # 리스트 컴프리헨션
g = (2 * i for i in range(1, 10)) # 제너레이터 표현식 (소괄호를 붙이면 제너레이터 객체생성)
show_all(st) # 2 4 6 8 10 12 14 16 18
show_all(g) # 2 4 6 8 10 12 14 16 18

def times2(): # 제너레이터 함수정의
    for i in range(1, 10):
        yield 2 * i
g = times2() # 제너레이터 객체 생성
show_all(g) # 2 4 6 8 10 12 14 16 18

g = (2 * i for i in range(1, 10))
print(next(g))
print(next(g))

def two():
    print('two')
    return 2

g = (two() * i for i in range(1, 10)) # 이때는 two함수 호출 안됨
print(next(g)) # two출력하고 2를 반환
print(next(g)) # two출력하고 4를 반환
print(next(g)) # two출력하고 6를 반환

# 제너레이터 표현식을 직접 전달하기
show_all((2 * i for i in range(1, 10)))

# 함수에 제너레이터 표현식을 바로 전달할 경우 소괄호 생략가능
show_all(2 * i for i in range(1, 10))
