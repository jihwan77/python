# 네임드 튜플
# 튜플에 이름을 부여하는 방법
from collections import namedtuple # collections 모듈의 namedtuple 함수 호출을 위해
# 튜플 -> namedtuple (클래스이름, 튜플의 값이름 리스트)
Tri = namedtuple('Triangle', ['bottom', 'height']) # 네임드 튜플 클래스 만듦
# 클래스도 객체
# 'Triangle'클래스명은 오류출력시 의미가 있다
t = Tri(3, 7) # 네임드 튜플 객체 생성
print(t[0], t[1]) # 일반 튜플과 동일한 방법으로 접근가능
print(t.bottom, t.height) # 이름으로 접근이 가능 (네임드 튜플이 갖는 장점)
# t[0] = 15 # TypeError: 'Triangle' object does not support item assignment
# 생성하는 방법
Tri = namedtuple('Tri', ['bottom', 'height']) # 권장하는 방법
Tri = namedtuple('Tri', 'bottom height')
# 네임트 튜플 언패킹
t = Tri(12, 79)
a, b = t
print(a, b) # 12 79

def show(n1, n2):
    print(n1, n2)

t = Tri(3, 8)
show(*t) # 함수호출시 언팩킹(풀어준다) 3 8