# 자료구조에서 중요
# 리스트 자료형 (순서O, 중복O, 수정O, 삭제O)
# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1]) #21000
print('d - ', d[-1]) #Captain
print('e - ', e[-1][1]) #Base
print('e - ', list(e[-1][1])) #['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>>>')
print('d - ', d[0:3]) # [1000, 10000, 'Ace']
print('d - ', d[2:]) # ['Ace', 'Base', 'Captine']
print('e - ', e[-1][1:3]) # ['Base', 'Captine']

# 리스트 연산
print('>>>>>>>')
print('c + d', c + d) # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']
print('c * 3', c * 3) # [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
print("'Test' + c[0]", 'Test' + str(c[0])) # Test70

# 값 비교
print(c == c[:3] + c[3:]) # True

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>>')
c[0] = 4
print('c - ', c) #[4, 75, 80, 85]
c[1:2] = ['a', 'b', 'c'] #  [['a', 'b', 'c']] list 안에  list 가 들어간다
print('c - ', c) #[4, 'a', 'b', 'c', 80, 85]
c[1] = ['a', 'b', 'c']
print('c - ', c) #[4, ['a', 'b', 'c'], 'b', 'c', 80, 85] 슬라이싱를 하지 않으면 list 안에  list 가 들어간다
c[1:3] = [] # 리스트가 삭제된다
print('c - ', c) #[4, 'c', 80, 85]
del c[2] # 삭제
print('c - ', c) #[4, 'c', 85]
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10) # 마지막에 데이타를 삽입
print('a - ', a) #[5, 2, 3, 1, 4, 10]
a.sort() # 정렬
print('a - ', a) #[1, 2, 3, 4, 5, 10]
a.reverse() #순서를 역순으로
print('a - ', a) #[10, 5, 4, 3, 2, 1]
print('a - ', a.index(3), a[3]) #3 3
a.insert(2, 7) # 위치, 추가할 값 (원래 있던것은 뒤로 밀어버린다)
print('a - ', a) #[10, 5, 7, 4, 3, 2, 1]
a.reverse()
print('a - ', a) #[1, 2, 3, 4, 7, 5, 10]
#del a[6]
a.remove(10)
print('a - ', a) #[1, 2, 3, 4, 7, 5]
print('a - ', a.pop()) # 5 스택구조 (last in fisrt out) 마지막의 원소를 가져오고 리스트에서 빠진다
print('a - ', a) #[1, 2, 3, 4, 7]
print('a - ', a.pop()) # 7 마지막의 원소를 가져오고 리스트에서 빠진다
print('a - ', a) #[1, 2, 3, 4]
# 큐구조 (fisrt in fisrt out)?
print('a - ', a.count(4)) #1 (리스트에 1이 중복되어 있는 갯수)
ex = [8, 9]
a.extend(ex)
print('a - ', a) #[1, 2, 3, 4, 8, 9]

# 삭제 : remove, pop, del

# 반복문
while a:
    data = a.pop()
    print(data) #9 ~ 1