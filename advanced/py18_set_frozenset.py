# 자료형 분류와 set & frozenset

# 시퀀스 타입 (저장순서가 유지되는 자료형)
# 리스트(list) 튜플(tuple) 레인지(range) 문자열(str)
# 인덱싱 연산 s[0] s[1]
# 슬라이싱 연산 s[0:3] 시작~부터 끝~까지

# 매핑 타입 (key, value를 가지고 데이타를 형성)
# 딕셔너리(dict) 순서나 위치정보를 기록하지 않는 자료형 (인덱싱, 슬라이싱 불가능)

# SET 타임 
# 셋(set), 프로즌셋(frozenset)
# 수학의 집합을 표현한 객체 (저장순서 유지하지 않음, 중복된 값의 저장 불가)
# set : mutable
# frozenset : immutable

# set, frozenset
# 합집합
# 차집합
# 교집합
# 대칭차집합

A = {'a', 'c', 'd', 'f'}
B = {'a', 'b', 'd', 'e'}

print(A - B) # 차집합 {'f', 'c'}
print(A & B) # 교집합 {'a', 'd'}
print(A | B) # 합집합 {'b', 'c', 'f', 'a', 'd', 'e'}
print(A ^ B) # 대칭차집합 (전체에서 교집합을 뺀것) {'b', 'f', 'e', 'c'}

A = set(['a', 'c', 'd', 'f']) # set함수에 iterable객체를 전달해서 set생성가능
B = set('fdca')
print(A) # {'c', 'f', 'd', 'a'}
print(B) # {'d', 'a', 'c', 'f'}
print(A == B) # True 저장순서는 상관없이 내용물만 같으면 True
print('a' in A) # True A집합에 'a'가 있는가?
print('b' not in A) # True A집합에 'b'가 없는가?
for c in A & B: # A & B의 결과로 얻은 집합을 대상으로 for 루프 구성
  print(c, end=' ') # f a c d
print()
d = {}
print(type(d)) # <class 'dict'>
s = set()
print(type(s)) # <class 'set'>

# frozenset 생성방법
A = frozenset(['a', 'c', 'd', 'f']) # frozenset함수에 iterable 객체를 전달
B = frozenset(['a', 'b', 'd', 'e'])
print(A - B) # 차집합 frozenset({'f', 'c'})

# set은 집합 : 중복된 값 제거
t = [3, 3, 3, 7, 7, 'z', 'z']
t = list(set(t))
print(t) # [3, 'z', 7]

# set 변경가능, forzenset 변경불가
# set : mutable 추가, 삭제 가능
# frozenset : immutable 추가, 삭제 불가

# add() 원소 추가하기
# discard() 원소 삭제하기
# update, != 다른집합의 원소 전부 추가
# intersection_update, &= 다른집합과 공통으로 있는 원소만 남기기
# difference_update, -= 다른집합이 갖는 원소 모두 삭제하기
# symmetic_difference_update, ^= 공통으로 갖기 않는것들은 추가하고 나머지는 삭제

os = {1, 2, 3, 4, 5}
os.add(6) # 6을 집합에 추가
print(os) # {1, 2, 3, 4, 5, 6}
os.discard(1) # 1을 집합에서 삭제
print(os) # {2, 3, 4, 5, 6}
os.update({7, 8, 9}) # {7, 8, 9}을 집합추가
# os |= {7, 8, 9} # {7, 8, 9}을 집합추가
print(os) # {2, 3, 4, 5, 6, 7, 8, 9}
os &= {2, 4, 6, 8} # {2, 4, 6, 8} 겹치는 원소만 남김
print(os) # {8, 2, 4, 6}
os -= {2, 4} # {2, 4} 원소 삭제
print(os) # {6, 8}
os ^= {1, 3, 6} # {1, 3, 6}에 있는 원소는 빼고 없는 원소는 추가
print(os) # {1, 3, 8}

# set 컴프리핸션
s1 = {x for x in range(1, 11)}
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s2 = {x ** 2 for x in s1}
print(s2) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
s3 = {x for x in s2 if x < 50}
print(s3) # {1, 4, 36, 9, 16, 49, 25}
