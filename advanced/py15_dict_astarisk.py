# 함수 호출과 매개변수 선언에 있어서 *와 **의 사용규칙
# iterable 객체와 매개변수
'''
  ( * 기본적으론 묶는다 -> 푼다 함수호출 인자 전달할때만)
def func(*args) 묶는다 : 함수를 정의하면서 매개변수 args에 *를 붙일때
func(*iterable) 푼다 : iterable객체를 전달하면서 *을 붙여서 함수 호출할 때

def func(*args) 함수를 정의하면서 매개변수 args에 **를 붙일때
func(**dict) dict객체를 전달하면서 **을 붙여서 함수 호출할 때
'''
def who(a, b, c):
  print(a, b, c, sep=', ')

# iterable객체에 *를 붙이면 풀어서 함수호출 인자에 전달
who(*[1, 2, 3]) # 1, 2, 3 list는 iterable객체 이므로 *를 붙일수 있다
who(*(0.1, 0.2, 0.3)) # 0.1, 0.2, 0.3 tuple도 iterable객체
who(*'str') # s, t, r str도 iterable객체

d = dict(a = 1, b = 2, c = 3)
# 함수호출 : dict *를 붙이면 key가 매개변수에 전달된다
who(*d) # a, b, c
# 함수호출 : dict **를 붙이면 value가 매개변수에 전달된다
who(**d) # 1, 2, 3

# 키와 값을 튜플로 묶어서 함수에 전달
who(*(d.items())) # ('a', 1), ('b', 2), ('c', 3)

# 딕셔너러와 매개변수
# 함수호출 -> **
# ** -> 함수정의
# def func(*args) 묶는다 : 튜플생성
# def func(**args) 묶는다 : 딕셔너리생성

def func(*args):
  print(args)
func() # ()
func(1) # (1,)
func(1, 2, 3) # (1, 2, 3) * 하나인경우 튜플로 묶어서 반환

def func_dic(**args):
  print(args)
func_dic(a = 1) # {'a': 1}
func_dic(a = 1, b = 2, c = 3) # {'a': 1, 'b': 2, 'c': 3}

def func_all(*args1, **args2):
  print(args1)
  print(args2)

func_all() # () {}
func_all(1, a = 1) # (1,) {'a': 1}
func_all(1, 2, 3, a = 1, b = 1) # (1, 2, 3) {'a': 1, 'b': 1}
