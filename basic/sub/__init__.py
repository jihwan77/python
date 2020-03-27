import sys
import inspect
# form ..sub2 import module2

# module1.py
def mod2_test1():
    print("Module2 -> Test1")
    print("Path : ", inspect.getfile(inspect.currentframe()))

def mod2_test2():
    print("Module2 -> Test2")
    print("Path : ", inspect.getfile(inspect.currentframe()))
