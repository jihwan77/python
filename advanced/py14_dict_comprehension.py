# dict 루핑 테크닉
# {key: value, key: value ....}
d = dict(a = 1, b = 2, c = 3)
for k in d: # k에는 key가 담긴다
    print(d[k], end=', ') # 1, 2, 3

# dict.keys()
# dict.values()
# dict.items()
# dict <--- view 객체  <<<< 리모콘 호출
# 뷰 객체도 iterable 객체로 for루프를 통해 참조가능
d = dict(a = 1, b = 2, c = 3)
for k in d.keys(): # keys는 뷰 객체를 반환함, 즉 뷰 객체를 통한 for루프
    print(k, end=', ') # 키가 순서대로 출력 -> a, b, c 

d = dict(a = 1, b = 2, c = 3)
for v in d.values(): # values는 뷰 객체를 반환함
    print(v, end=', ') # 값이 순서대로 출력 -> 1, 2, 3 

d = dict(a = 1, b = 2, c = 3)
for kv in d.items(): # items는 뷰 객체를 반환함
    print(kv, end=', ') # (키, 값)이 순서대로 출력 -> ('a', 1), ('b', 2), ('c', 3)

# 언팩킹
d = dict(a = 1, b = 2, c = 3)
for k, v in d.items(): # k와 v에 값을 저장하는 과정에서 튜플 언팩킹
    print(k, v, sep=', ') # 'a', 1 'b', 2 'c', 3
print()

# 뷰가 바라보는 현재상태
# view는 dict를 바라보고 있다  dict <---- view
# view가 생성되는 시점이 아니라 리모콘(iterator)객체가 생성되는 시점이 중요하다
d = dict(a = 1, b = 2, c = 3)
vo = d.items()
for kv in vo:
    print(kv, end=' ') # ('a', 1) ('b', 2) ('c', 3)
print()
d['a'] += 3 # 딕셔너리 수정
d['c'] -= 2 # 딕셔너리 수정
for kv in vo: # 수정 사항이 뷰 객체에 그대로 반영됨 
    print(kv, end=' ') # ('a', 4) ('b', 2) ('c', 1)
print()

# dict 컴프리핸션
# map
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1]
print(r2)

d1 = dict(a = 1, b = 2, c = 3)
# d1.items() => ('a', 1) => k, v로 언팩킹 => 'a': 2
d2 = {k : v * 2 for k, v in d1.items()} # d1의 값을 두 배 늘린 딕셔너리 생성
d3 = {k : v * 2 for k, v in d2.items()} # d2의 값을 두 배 늘린 딕셔너리 생성
print(d1) # {'a': 1, 'b': 2, 'c': 3}
print(d2) # {'a': 2, 'b': 4, 'c': 6}
print(d3) # {'a': 4, 'b': 8, 'c': 12}

# filter
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1 if x % 2]
print(r2) # [2, 6, 10]

d1 = dict(a = 1, b = 2, c = 3, d = 4)
d2 = {k : v for k, v in d1.items() if v % 2} # d1에서 값이 홀수인 것만 모은 딕셔너리
print(d1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d2) # {'a': 1, 'c': 3}

# zip
ks = ['a', 'b', 'c', 'd'] # key
vs = [1, 2, 3, 4] # value
d = {k : v for k, v in zip(ks, vs)}
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

ks = ['a', 'b', 'c', 'd'] # key
vs = [1, 2, 3, 4] # value
d = {k : v for k, v in zip(ks, vs) if v % 2}
print(d) # {'a': 1, 'c': 3}