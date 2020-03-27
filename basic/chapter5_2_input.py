# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)
'''
# 예제1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company Name : ")

print(name, grade, company)

# 예제2
number = input("Enter number : ")
name = input("Enter Your Name : ")

print('type of number', type(number), number * 3) # <class 'str'> 555
print('type of name', type(name), name)

# 예제3
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print('first_number + second_number : ', total)

# 예제4
float_number = float(input("Enter a float number : "))
print("input float : ", float_number * 1.2113)
print("input type : ", type(float_number))

# 예제5
'''
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))