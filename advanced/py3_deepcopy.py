# 깊은복사와 얕은복사

# v1 == v2 내용비교(값비교)
# v1 is v2 동등 동일한 객체인가(참조주소값비교)

r1 = [1, 2, 3]
r2 = [1, 2, 3]
print(r1 is r2) # False
print(r1 == r2) # True
r2 = r1
print(r1 is r2) # True

# 'Jone' 문자열 불변
# ('man', 'USA') 튜플 불변
# [175, 23] 리스트 변경가능
# 불변의 경우는 복사를 해도 문제가 되지 않는다. (공유해도 상관없다)
# 리스트 객체 같이 변경이 가능한 객체는 공유하면 문제가 될 수 있다
r1 = ['Jone', ('man', 'USA'), [175, 23]]
r2 = list(r1) # 파이썬은 얕은 복사를 한다(리스트 안의 객체는 공유한다)
print(r1 is r2) #False
print(r1[0] is r2[0]) #True
print(r1[1] is r2[1]) #True
print(r1[2] is r2[2]) #True

# 깊은복사 (리스트가 참조하는 객체까지 복사하는 개념)

# 깊고 얕은 복사
# 가변은 깊은 복사를 불변은 얕은 복사를 하는것
# copy.deepcopy() 가 알아서 해준다
import copy
J2021 = ['Jone', ('man', 'USA'), [175, 23]]
J2022 = copy.deepcopy(J2021)
J2022[2][1] += 1    # 한살 더 먹음
print(J2021)
print(J2022) # ['Jone', ('man', 'USA'), [175, 24]]

# 튜플이나 문자열을 복사하면 얕은 복사가 진행된다
# (리스트는 깊은 복사)
d1 = (1, 2, 3)
d2 = 'Please'
c1 = tuple(d1)
c2 = str(d2)
print(d1 is c1) # True 복사를 해도 참조값은 같다
print(d2 is c2) # True