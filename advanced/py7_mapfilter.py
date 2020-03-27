# 맵 map 과 필터 filter
# map
def pow(n):
    return n ** 2

st1 = [1, 2, 3]

st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])] # X
st2 = [pow(x) for x in st1] # X
print(st2) # [1, 4, 9]

# map의 매개변수 (1.함수, 2.iterable객체)
# map이 반환하는 객체는 iterator이다.
st2 = list(map(pow, st1)) # list함수에 iterator객체 전달가능
# st2 = list(map(lambda n: n ** 2, [1, 2, 3]))
print(st2) # [1, 4, 9]

st = [1, 2, 3]
ir = map(pow, st) #반환객체는 iterator객체
for i in ir:
    print(i, end=' ')

# map : iterable객체면 무엇이든 전달이 가능
def dbl(e):
    return e * 2
print(list(map(dbl, (1, 3, 4))))
print(list(map(dbl, 'hello')))

def sum(n1, n2):
    return n1 + n2
st1 = [1, 2, 3]
st2 = [3, 2, 1]

# sum함수는 매개변수가 두개
#  따라서 map의 두번째, 세번째 매개변수에 필요한 iterator객체를 넣는다
st3 = list(map(sum, st1, st2)) 
print(st3)

# map과 람다
st = [1, 2, 3, 4, 5, 6, 7, 8]

print(st[ : ]) # 처음부터 끝까지
print(st[ : :1]) # 처음부터 끝까지 한 칸씩 [1, 2, 3, 4, 5, 6, 7, 8]
print(st[ : :2]) # 처음부터 끝까지 두 칸씩 [1, 3, 5, 7]
print(st[ : :3]) # 처음부터 끝까지 세 칸씩 [1, 4, 7]
# 리스트나 문자열등을 뒤집는것
print(st[ : :-1]) # 처음부터 끝까지 역순으로 한 칸씩 [8, 7, 6, 5, 4, 3, 2, 1]
s = 'hello'
print(s[ : :-1]) #olleh

st = ['one', 'two', 'three']

def rev(s):
    return s[ : :-1]
rst = list(map(rev, st))
print(rst) #['eno', 'owt', 'eerht']
# 람다로 표현하면 함수를 정의하지 않아도 되며
# 함수가 끝나자마자 레퍼런스카운트가 0이되어 가비지컬렉션 대상이 된다
rst = list(map(lambda s: s[ : :-1], st))
print(rst) #['eno', 'owt', 'eerht']

# filter
# filter 함수는 값을 걸러내는 기능을 제공하는 함수
# filter 함수의 첫번째 인자는 조건에 따라서 True나 False를 리턴하도록 정의
def is_odd(n):
    return n % 2 # 홀수이면 True반환
st = [1, 2, 3, 4, 5]
ost = list(filter(is_odd, st))
print(ost) # [1, 3, 5]

# 람다식
ost = list(filter(lambda n: n % 2, st))
print(ost) # [1, 3, 5]

# 3의 배수만 담는 예제
st = list(range(1, 11))
fst = list(filter(lambda  n: not(n % 3), st))
print(fst) # [3, 6, 9]

st = list(range(1, 11))
# map이 반환하는 iterator객체를 filter의 두번째 매개변수로 전달
# 1~10 제곱값중 3의 배수만 담는 예제
fst = list(filter(lambda n: not(n % 3), map(lambda n: n ** 2, st)))
print(fst) # [9, 36, 81]