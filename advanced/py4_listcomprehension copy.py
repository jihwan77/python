# 리스트 컴프리핸션
# 리스트 생성방법
r1 = [1, 2, 3]
r2 = []
r3 = [1, 2, [3, 4]] # 리스트가 포함된 리스트 생성

r4 = list('Hello') # 문자열을 전달해서 리스트 생성
r5 = list((5, 6, 7)) # 튜플을 전달해서 리스트 생성
r6 = list(range(0, 5)) # 레인지를 전달해서 리스트 생성

# 리스트의 생성과 리스트를 채우는 과정이 분리되어 있다는 과정이 불편하다
r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:
    r2.append(i * 2)
print(r2) # [2, 4, 6, 8, 10]

# 리스트의 생성과 리스트를 채우는 과정을 하나로 묶는방법이
# 리스트 컴프리핸션
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1]
print(r2) # [2, 4, 6, 8, 10]

# 리스트를 구성하는 객체들에 대한 기본정보가 주어지고 그 뒤에 세세한 정보가 뒤에 나온다
# 1. x * 2 | 2. for x in r1
# 1. 리스트를 채울 데이타가 무엇인지 알려주는 값 (x * 2)
#  - 이 리스트의 값은 x * 2의 결과들로 이루어진다
# 2. x값이 무엇인지 정보가 들어간다
#  - x는 r1에 있는 값들이다
# r1의 값들을 하나씩 x에 넣어서, x * 2의 결과를 만들어 리스트에 저장

# 조건 필터 생성방법
r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:
    if i % 2: # i가 홀수인경우 (0이 아닌경우만 True)
        r2.append(i * 2)
print(r2) # [2, 6, 10]

# 리스트 컴프리핸션
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1 if x % 2]
print(r2)

# [1. x * 2 | 2. for x in r1 if x % 2]
# 1. r2를 채우는 리스트들은 x * 2로 이루어 집니다.
# 2. x는 r1에서 하나씩 가져다가 씁니다
#  단, 조건이 홀수(True)인 경우에만 1.로 보내서 리스트를 채움니다.


# 리스트 컴프리헨션에 for 한번더 들어가는 경우
r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = []
for t in r1:
    for p in r2:
        r3.append(t + p)
print(r3)

# 리스트 컴프리핸션
r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = [t + p for t in r1 for p in r2]
print(r3)
# [1. t + p | 2. for t in r1 for p in r2]

# 구구단
r = [n * m for n in range(2, 10) for m in range(1, 10)]
print(r)

# 다중 for 루프에 조건 필터 추가
# 결과가 홀수 인경우만 담는로직
r = [n * m for n in range(2, 10) for m in range(1, 10) if (n * m) % 2]
print(r)