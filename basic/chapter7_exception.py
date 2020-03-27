# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
#print('error) # SyntaxError: EOL while scanning string literal
#if True # SyntaxError: invalid syntax
#    pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c) # NameError: name 'c' is not defined

# ZeroDivisionError
# print(100/0) # ZeroDivisionError: division by zero

# IndexError
# x = [50, 70, 90]
# print(x[5]) # IndexError: list index out of range
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # IndexError: pop from empty list

# KeyError
# dic = {'name': 'Lee', 'age': 41, 'city': 'Busan'}
# print(dic['hobby']) # KeyError: 'hobby'
# print(dic.get('hobby')) # None

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권잔(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2()) # AttributeError: module 'time' has no attribute 'time2'

# ValueError
# x = [10, 50, 90]
# x.remove(200) # ValueError: list.remove(x): x not in list

# FileNotFoundError
# f = open('test.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) # TypeError: can only concatenate list (not "tuple") to list
# print(x + z) # TypeError: can only concatenate list (not "str") to list
print(x + list(y))
print(x + list(z))

# 예외 처리 기본
# try : 예러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 여러개 가능
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# 예제1
# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Kim' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# print()
# print('pass')

# 예제2
# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Kim' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except: # 모든 예외를 잡지만 무슨예외인지 알수 없음 (except: == except Exception:)
#     print('Not found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# print()
# print('pass')

# 예제3
# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Cho' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError as e: # 모든 예외를 잡지만 무슨예외인지 알수 없음 (except: == except Exception:)
#     print(e)
#     print('Not found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finallly!')

    
# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError('error')
except ValueError as e:
    print(e)
    print('Occurred! ValueError!')
else:
    print('Ok! else!')



    