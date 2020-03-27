# immutable 튜플, mutable 리스트
# 리스트는 변경이 가능하다
r = [1, 2]
print(r, id(r))
r += [3, 4]
print(r, id(r)) # list는 객체의 주소값이 변하지 않는다.
# 튜플은 변경이 불가능하다
t = (1, 2)
print(t, id(t))
t += (3, 4)
print(t, id(t)) # tuple는 새로운 객체가 만들어지며 기존 (1, 2)값은 레퍼런스카운트가 0이 되어 가비지 컬렉션 대상이다.

def add_last(m, n):
    m += n
r = [1, 2]
add_last(r, [3, 4])
print(r) # [1, 2, 3, 4]
t = (1, 3)
add_last(t, (5, 7)) # m은 (1, 3, 5, 7)이되지만 새로운 객체가 만들어진다.
print(t) # t는 (1, 3)값을 그대로 참고 하고 있음

def add_tuple(t1, t2):
    t1 += t2 # t1에 새로운 튜플이 저장됨
    return t1 #새로운 튜플을 반환
tp = (1, 3)
tp = add_tuple(tp, (5, 7))
print(tp) # (1, 3, 5, 7)

def min_max(d):
    d.sort() # 리스트를 오름차순으로 정렬
    print(d[0], d[-1], sep=', ') # 맨 앞, 마지막값을 출력
l = [3, 1, 5, 4]
min_max(l)
print(l) # 이런 원본의 순서가 변경되었음

def min_max2(d):
    d = list(d) # d의 새로운 리스트 생성 (튜플도 리스트로 변환가능)
    d.sort() # 원본이 아닌 복사본을 정렬
    print(d[0], d[-1], sep=', ') 
l = [3, 1, 5, 4]
min_max2(l)
print(l) # 원본이 수정되지 않았음
t = (3, 1, 5, 4)
min_max2(t)
print(t) # 튜플 대상으로도 잘동작함
