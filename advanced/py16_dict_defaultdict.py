# dict & defaultdict

# 키가 존재할 때와 존재하지 않을때

# 키가 존재할때 값을 수정
d = {'red': 3, 'white': 2, 'blue': 4}
d['red'] = 1 # 키 'red' 값을 1로 변경
print(d) # {'red': 1, 'white': 2, 'blue': 4}

# 키가 존재하지 않는 경우 -> 새로운 키와 값이 추가
d = {'white': 2, 'blue': 4}
d['red'] = 1 # 'red': 1 추가
print(d) # {'white': 2, 'blue': 4, 'red': 1}

# 저장되어 있는 값을 참조해서 연산을 하는경우
# 키가 존재할때
d = {'red': 3, 'white': 2, 'blue': 4}
d['red'] += 1 # 키 'red' 값을 1증가
print(d) # {'red': 4, 'white': 2, 'blue': 4}

# 키가 존재하지 않는 경우 -> KeyError 예외
d = {'white': 2, 'blue': 4}
#d['red'] += 1 # 키 'red' 값을 1증가
# print(d) # 키가 존재하지 않는다면 예외발생 KeyError: 'red'

s = 'robbot'
d = {}
for k in s:
  if k in d: # 키가 존재하면 값 1증가
    d[k] += 1
  else: # 키가 존재하지 않으면 키의 값을 1로 해서 추가
    d[k] = 1
print(d) # {'r': 1, 'o': 2, 'b': 2, 't': 1}

# setdefault 메소드
# d.setdefault(k, v) 매개변수 k에는 키, v에는 디폴트 값
# 키가 없으면 : 디폴트 값으로 등록하여 반환
# 키가 있으면 : 값을 반환
s = 'robbot'
d = {}
for k in s:
  d[k] = d.setdefault(k, 0) + 1
print(d) # {'r': 1, 'o': 2, 'b': 2, 't': 1}

# defaultdict 딕셔너리 
# 디폴트 함수를 장작한 메소드
# k라는 키를 달라고 했는데 없으면 값을 디폴트 함수를 통해 가져와서 만든다
from collections import defaultdict #defaultdict은 collections모듈의 함수임
s = 'robbot'
d = defaultdict(int) # int() 디폴트 함수로 등록하면서 defaultdict 호출
for k in s:
  d[k] += 1
print(d) # defaultdict(<class 'int'>, {'r': 1, 'o': 2, 'b': 2, 't': 1})
print(d['r'], d['o'], d['b'], d['t'], sep=', ')  # 1, 2, 2, 1 일반적인 딕셔너리와 참조방법도 같다

n1 = int('36')
print(n1) # '36' -> 36
n2 = int() 
print(n2) # 0

def ret_zero():
  return 0

d = defaultdict(ret_zero) # ret_zero() 디폴트 함수로 등록하면서 defaultdict 호출
print(d['a']) # 해당 키 없으므로 'a': 0 등록됨
print(d) # defaultdict(<function ret_zero at 0x000001C39FD4DA60>, {'a': 0})

# lambda로 변경
d = defaultdict(lambda: 7) 
print(d['a']) # 7
print(d) # defaultdict(<function <lambda> at 0x000001C8E0496040>, {'a': 7})
