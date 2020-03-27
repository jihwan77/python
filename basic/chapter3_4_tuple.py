# 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서O, 중복O, 수정X, 삭제X) # 불변(한번 선언하면 끝까지 쓰는것)

# 선언 튜플을 (선언할때 () 는 있어도 되고 없어도 되지만 관례상 ()로 묶는다)
a = ()
b = (1) # b = (1,) 원소가 하나일경우 ,를 찍어서 tuple형으로 선언가능함
print(type(a), type(b)) # <class 'tuple'> <class 'int'> 원소가 하나인경우 int이므로 주의
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>')
print('d - ', d[1]) #1000
print('d - ', d[0] + d[1] + d[1]) #2100
print('d - ', d[-1]) #Captine
print('e - ', e[-1]) #('Ace', 'Base', 'Captine')
print('e - ', e[-1][1]) #Base
print('e - ', list(e[-1][1])) #['B', 'a', 's', 'e'] 리스트로 형변환 하는 순간 수정, 삭제가 가능함

#수정 X
#d[0] = 1500 # 'tuple' object does not support item assignment

#슬라이싱
print('>>>>')
print('d - ', d[0:3]) #(100, 1000, 'Ace')
print('d - ', d[2:]) #('Ace', 'Base', 'Captine')
print('e - ', e[2][1:3]) #('Base', 'Captine')

#튜플연산
print('>>>>>')
print('c + d', c + d)#(11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3', c * 3)#(11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)

#튜플함수
a = (5, 2, 3, 1, 2)
print('a - ', a)
print('a - ', a.index(3)) #2 3의 위치
print('a - ', a.count(2)) #2 2가 두개

#패킹 & 언패킹 (Packing, and Unpacking)

#패킹
t = ('foo', 'bar', 'baz', 'qux') #패킹

#언패킹 (하나로 되어있는 튜플을 각각 변수에 담는다)
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

#패킹 & 언패킹
t2 = 1, 2, 3 #패킹 괄호는 생략해도 된다
t3 = 4, #패킹 
x1, x2, x3 = t2 #언패킹
x4, x5, x6 = 4, 5, 6 #언패킹 x4, x5, x6 = (4, 5, 6)

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)