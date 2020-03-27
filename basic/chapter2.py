# 기본선언
n = 700
print(n)
print(type(n))

# 동시선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = 'Change Value'

# 출력
print(var)
print(type(var))

# object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력
print(300)
print(int(300))

# n -> 777
n = 777
print(n, type(n))

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400

print(m, n)
print(type(m), type(n))

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n)) #False

m = 800
n = 400 * 2

print(id(m))
print(id(n))
print(id(m) == id(n)) #True

# 다양한 변수 선언
# Camel Case : numberOfCollageGraduates -> Method
# Pascal Case : NumberOfCollageGraduates -> Class
# Snake Case : number_of_collage_graduates 

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 숫자나 다른 특수기호는 앞에 올수 없다(단, _과 $는 앞에 올 수 있음)

# 예약어는 변수명으로 불가능
# for as class import

