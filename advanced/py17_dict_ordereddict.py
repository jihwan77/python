# dict & OrderedDict
# dict은 저장 순서를 유지하기 시작했다
# (집합처럼 순서를 보장받지 못하는 자료구조였지만 파이썬 3.7부터는 순서를 보장해주고있다)
# dict은 저장순서는 정보로 판단안한다
# OrderedDict은 *저장순서* 도 정보로 판단한다
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) # {'a': 1, 'b': 2, 'c': 3}
for kv in d.items():
  print(kv) # ('a', 1) ('b', 2) ('c', 3)

from collections import OrderedDict # collections모듈의 OrderedDict
od = OrderedDict() # OrderedDict 객체 생성
od['a'] = 1 # 딕셔너리 사용 방법과 동일
od['b'] = 2
od['c'] = 3
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for kv in od.items():
  print(kv) # ('a', 1) ('b', 2) ('c', 3)

# 그래도 OrderedDict을 써야 할 이유가 있다면?
d1 = dict(a = 1, b = 2, c = 3)
d2 = dict(c = 3, a = 1, b = 2)
print(d1) # {'a': 1, 'b': 2, 'c': 3}
print(d2) # {'c': 3, 'a': 1, 'b': 2}
print(d1 == d2) # True 저장순서는 다르고 내용물은 같다

od1 = OrderedDict(a = 1, b = 2, c = 3) # dict 객체의 생성 방법과 동일
od2 = OrderedDict(c = 3, a = 1, b = 2) 
print(od1) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od2) # OrderedDict([('c', 3), ('a', 1), ('b', 2)])
print(od1 == od2) # False 각각의 데이타의 존재는 일치하지만 저장순서에 대한 정보가 다르다


od = OrderedDict(a = 1, b = 2, c = 3) # dict 객체의 생성 방법과 동일
print(dict(od)) # {'a': 1, 'b': 2, 'c': 3}

od.move_to_end('b') # 키가 'b'인 키와 값을 맨 뒤로 이동
print(dict(od)) # {'a': 1, 'c': 3, 'b': 2}

od.move_to_end('b', last=False) # 매개변 last에 False를 전달하면 맨 앞으로 이동
print(dict(od)) # {'b': 2, 'a': 1, 'c': 3}