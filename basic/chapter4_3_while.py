# while <expr>:
#   <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1
print()
# 예제2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())
print()
# 예제3 if중첩
# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# continue
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

#
i = 1
while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# while - else 구문
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

# 예제
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        print('find!')
        break
    i += 1
else:
    print(s, 'not found in list.')

# 무한반복
#while True:
#    print('foo')

# 예제
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())
