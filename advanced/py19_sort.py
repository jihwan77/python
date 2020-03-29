# 정렬기술
# sort함수
# 리스트 자체를 변경시킨다
ns = [3, 1, 4, 2]
ns.sort() # 기본 오름차순
print(ns) # [1, 2, 3, 4]

ns = [3, 1, 4, 2]
ns.sort(reverse=True) # 내림차순 정렬
print(ns) # [4, 3, 2, 1]

# 튜플 : 나이를 기준으로 오름차순 정렬
ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
def age(t): # 나이 반환하는 함수
  return t[1]
def name(t): # 이름을 반환하는 함수
  return t[0]
ns.sort(key = age) # 매개변수 key에 함수 age를 전달
# ns.sort(key = name) # 매개변수 key에 함수 name를 전달
# ns.sort(key = age, reverse=True) # 나이를 기준으로 내림차순 정렬
print(ns) # [('Lee', 12), ('Park', 29), ('Yoon', 33)]

# 람다로 표현 튜플 나이를 기준으로 내림차순 정렬
ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
ns.sort(key = lambda t: t[1], reverse=True)
print(ns) # [('Yoon', 33), ('Park', 29), ('Lee', 12)]

# 문자열의 길이로 정렬 (len함수이용)
names = ['Julia', 'Yoon', 'Steven']
names.sort(key = len)
print(names) # ['Yoon', 'Julia', 'Steven']

# 두수의 합이 큰수부터 정렬
nums = [(3, 1), (2, 9), (0, 5)]
nums.sort(key = lambda t: t[0] + t[1], reverse=True)
print(nums) # [(2, 9), (0, 5), (3, 1)]

# sorted 함수 사용법
# 원본은 그래로 두고 정렬된 사본을 얻는다
org = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
cpy = sorted(org, key=lambda t: t[1], reverse=True) # 나이기준 내림차순
print(org) # 원본유지 [('Yoon', 33), ('Lee', 12), ('Park', 29)] 
print(cpy) # 정렬된 사본생성 [('Yoon', 33), ('Park', 29), ('Lee', 12)]

# 튜플이나 문자열등 immutable객체인 경우도 iterable객체라면 sorted 함수로 정렬이 가능하다
# 주의) sorted함수를 통과하면 리스트로 리턴된다
org = (3, 1, 2)
cpy = sorted(org) # 정렬한 결과는 리스트
cpy2 = tuple(sorted(org)) # 튜플로 변환
print(org) # (3, 1, 2)
print(cpy) # [1, 2, 3]
print(cpy2) # (1, 2, 3)

org = ('3212', '214', '197000')
cpy = tuple(sorted(org, key= lambda s: int(s)))
cpy2 = tuple(sorted(org))
print(cpy) # ('214', '3212', '197000')
print(cpy2) # ('197000', '214', '3212')