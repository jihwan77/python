# 모듈 사용 실습
import sys
# sys.path는 list 타입이므로 아래와같이 append할수 있다
# sys.path.append('C:\\workspace\\python\\module')

# import time
# import test_module

print(sys)
print(sys.path)
# print(time.time())

print(type(sys.path))
import chapter6_2_module
print(chapter6_2_module.power(10, 3))
# print(test_module.power(10, 3))
