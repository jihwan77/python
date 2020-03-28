# 튜플의 패킹과 언패킹
# 튜플 패킹 : 묶기 (하나 이상의 값을 튜플로 묶는 행위)
# 튜플 언패킹 : 풀기 (튜플에 묶여 있는 값들을 풀어내는 행위)
# * : 묶는다. 
#     단, 함수의 인자를 전달할때 풀기
tri_one = (12, 15) # 튜플 생성 == 튜플 패킹
tri_two = 12, 15 # 튜플 패킹은 소괄호가 없어도 됨
tri_three = (12, 25)
bt, ht = tri_three # 튜플 언패킹 (저장된 값과 이를 저장할 변수의 수가 일치)

nums = (1, 2, 3, 4, 5)
n1, n2, *others = nums # 둘 이상의 값을 리스트로 묶을 때 *를 사용한다
print(n1, n2, others) # 1 2 [3, 4, 5] 주의) others값은 리스트로 묶인다

nums = (1, 2, 3, 4, 5)
first, *others, last = nums 
print(first, others, last) # 1 [2, 3, 4] 5

nums = (1, 2, 3, 4, 5)
*others, n1, n2 = nums 
print(others, n1, n2) # [1, 2, 3] 4 5

nums = [1, 2, 3, 4, 5]
n1, n2, *others = nums # 리스트도 언패킹이됨
print(n1, n2, others) # 1 2 [3, 4, 5]

def ret_nums():
    return 1, 2, 3, 4, 5 # 튜플로 반환이 가능, 튜플은 소괄호가 생략된 형태이다. (패킹되서 반환)
nums = ret_nums()
print(nums) # (1, 2, 3, 4, 5)

n, *others = ret_nums()
print(n, others) # 1 [2, 3, 4, 5] 리스트로 묶인다

# * : 묶는다. 
# * : 푼다 (함수 호출)
def show_nums(n1, n2, *other):
    print(n1, n2, other, sep=', ') # 1, 2, (3, 4, 5)
show_nums(1, 2, 3, 4, 5)

def sum(*nums): # 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장
    s = 0
    for i in nums:
        s += i
    return s

print(sum(1, 2, 3)) # 6
print(sum(1, 2, 3, 4)) # 10

def show_man(name, age, height):
    print(name, age, height, sep=', ')

p = ('Yoon', 22, 180)
show_nums(*p) # 푼다 : 함수 호출할 때 *는 풀어서 각각의 매개변수에 전달 Yoon, 22, 180
p = ['Park', 21, 177] # 리스트도 동일하게 사용
show_nums(*p) # Park, 21, 177

# 튜플안에 튜플이 있는경우
t = (1, 2, (3, 4))
a, b, (c, d) = t
print(a, b, c, d, sep=', ') # 1, 2, 3, 4

p = 'Hong', (32, 178), '010-1234-5xxx', 'Korea'
na, (ag, he), ph, ad = p
print(na, he) # Hong 178

# 실제 필요한 정보(이름, 키)만 뽑아내는 방법 (불필요한 변수선언 X)
na, (_, he), _, _ = p
print(na, he)

# for 루프에서의 언패킹
ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]
for n, h in ps:
    print(n, h, sep=', ') # Lee, 172 Jung, 182 Yoon, 179

ps = (['Lee', 172], ['Jung', 182], ['Yoon', 179]) # 리스트도 언패킹가능
for n, h in ps:
    print(n, h, sep=', ') # Lee, 172 Jung, 182 Yoon, 179
