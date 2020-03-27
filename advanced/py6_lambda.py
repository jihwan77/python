# 파이썬에서는 함수도 객체 그리고 람다

# 모든건 객체다
x = 3.0
type(x) # <class 'float' >
print(x.is_integer())

def func1(n):
    return n
def func2():
    print('Hello')

print(type(func1)) # <class 'function'>

def say1():
    print('Hello')
def say2():
    print('안녕하세요')
def caller(fct):
    fct()
caller(say1) # 함수의 매개변수로 함수를 전달 가능 (함수가 객체이기 때문에)
caller(say2)

# 함수내에서 함수를 만들어서 반환할 후 있다
def fct_fac(n):
    def exp(x): # 함수 내에 함수정의
        return x ** n
    return exp

f2 = fct_fac(2) # f2는 제곱을 반환하는 함수
f3 = fct_fac(3) # f3는 세제곱을 반환하는 함수
print(f2(4))
print(f3(4))

print(fct_fac(2)(4)) # 이렇게도 표현이 가능

# 이름 없는 함수의 정의
# 함수의 이름이 존재하는 이유는 함수를 호출하는것이 목적
# exp함수는 함수이름으로 호출하지 않았고 반환하기 위한 목적으로 만들었다

# lambda (함수이름 불필요 반환이라는 목적만 해결)

def show(s):
    print(s)
ref = show # 이름을 하나 더붙이는것
ref('Hi~')
print('>>>>>>>>>>>>>>')

ref = lambda s: print(s) # 람다 기반의 함수 정의
ref('Oh~')

# ref - 참조변수 = lambda s - 매개변수: print(s) - 함수몸체
# lambda args: expression
# 연산의 결과 값이 함수의 반환값이 된다 (return 키워드X)
f1 = lambda n1, n2: n1 + n2
print(f1(3, 4))
# 함수가 값을 반환하면 그값이 반환된다 (return 키워드X)
f2 = lambda s: len(s)
print(f2('simple'))
# 매개변수가 없는 함수
f3 = lambda : print('yes ~')
f3()

# 람다식으로 기존 함수 변경
def fct_fac2(n):
    return lambda x: x ** n
f2 = fct_fac2(2) # f2는 제곱을 반환하는 함수
f3 = fct_fac2(3) # f3는 세제곱을 반환하는 함수
print(f2(4))
print(f3(4))