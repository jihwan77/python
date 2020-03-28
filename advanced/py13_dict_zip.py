# dict의 생성과 zip
print(type({})) # <class 'dict'>

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict([('a', 1), ('b', 2), ('c', 3)])
d3 = dict(a = 1, b = 2, c = 3) # 키가 문자열인 경우 딕셔너리 생성방법
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3])) # 키와 값을 별도로 묶어서 딕셔너리 생성
print(d1) # {'a': 1, 'b': 2, 'c': 3}
print(d1 == d2 == d3 == d4) # True

# 딕셔너리는 저장순서를 보장하지 않는다 (집합)
# 그러나, 3.7부터 파이썬은 저장 순서를 보장하고 있다

d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k in d:
    print(d[k], end=', ') # 1, 2, 3, 4,

print()

# zip 함수
# 빵 10개, 우유 10개 -> 10개의 봉지에 하나씩 나눠 담는다. 분배하기 쉽도록
z = zip(['a', 'b', 'c'], [1, 2, 3]) # 두개의 리스트에 저장된 값들을 조합
for i in z:
    print(i, end=', ') # ('a', 1), ('b', 2), ('c', 3),
print()
z = zip(('a', 'b', 'c'), (1, 2, 3)) # 두개의 튜플에 저장된 값들을 조합
for i in z:
    print(i, end=', ') # ('a', 1), ('b', 2), ('c', 3),
print()
z = zip('abc', (1, 2, 3)) # 문자열과 튜플에 저장된 값들을 조합
for i in z:
    print(i, end=', ') # ('a', 1), ('b', 2), ('c', 3),
print()
d = list(zip(['a', 'b', 'c'], [1, 2, 3])) # zip과 list의 조합
print(d) # [('a', 1), ('b', 2), ('c', 3)]
d = tuple(zip('abc', '123')) # zip과 tuple의 조합
print(d) # (('a', '1'), ('b', '2'), ('c', '3'))
d = dict(zip(['a', 'b', 'c'], [1, 2, 3])) # zip과 dict의 조합
print(d) # {'a': 1, 'b': 2, 'c': 3}

c = list(zip('abc', (1, 2, 3), ['one', 'two', 'three'])) # 셋 이상의 값들을 조합
print(c) # [('a', 1, 'one'), ('b', 2, 'two'), ('c', 3, 'three')]

