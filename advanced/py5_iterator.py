# Iterable객체와 Iterator객체

ds = [1, 2, 3, 4]
for i in ds:
    print(i, end=' ')

# Iterable객체 : Iterator객체를 만들수 있는 객체 
#  - iter 함수에 인자로 전달 가능한 객체 (list, str, tuple ..)
# Iterator객체 : iter()함수로 생성하고 next()함수로 접근
#  - iter 함수가 생성해서 반환하는 객체

# iter함수
ds = [1, 2, 3]
ir = iter(ds) # iterator객체를 얻는 방법
print(next(ir)) # 값을 하나 꺼내는 방법
print(next(ir))
print(next(ir))
# print(next(ir)) # 마지막 값을 이미 반환했으므로 StopIteration 예외가 발생

# 원하는 시점에 next함수를 호출하여 결과를 받아 올 수 있다
# itearble객체를 대상으로 iter함수를 호출하여 iterator객체를 만든다
# iterator객체를 생성할 수 있는 대상이 되는 것이 iterable객체이다

# 스페셜 메소드
# 위 예제의 실제 함수 호출 형태는 아래와 같다
# ir = iter(ds) -> ds.__iter__()
# next(ir) -> ir.__next__()
ds = [1, 2, 3]
ir = ds.__iter__() # iterator객체를 얻는 방법
print(ir.__next__()) # 값을 하나 꺼내는 방법
print(ir.__next__())

# Iterable객체의 종류와 확인 방법
# list, tuple, str ...
# Iterable객체 확인방법
print(dir([1, 2])) # __iter__ 메소드가 존재하는지 확인하는 방법
print(hasattr([1, 2], '__iter__'))

for i in [1, 2, 3]:
    print(i, end=' ')

# 내부적으로 아래와 같이 수행한다
# for문의 반복의 대상이 되려면 Iterable객체여야 한다.
ir = iter([1, 2, 3])
while True:
    try:
        i = next(ir)
        print(i, end=' ')
    except StopIteration:
        break
# 그런데 for 루프에 Iterable객체가 아닌 Iterator 객체를 두어도 정상동작한다.
ir = iter([1, 2, 3])
for i in ir:
    print(i, end=' ')

# Iterator객체도 iter() 인자로 들어갈수 있으므로 Iterable객체이다
# iter([1, 2, 3, 4])함수에 Iterator객체를 전달하면 Iterator객체를 그대로 리턴
ir1 = iter([1, 2, 3])
ir2 = iter(ir1)
print(ir1 is ir2) # True
