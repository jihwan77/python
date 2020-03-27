#문자열생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are You?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

#빈 문자열
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
#I'm Boy
print("I\'m Boy")
print('I\'m Boy')
print('a \t b') #탭
print('a \n b') #줄바꿈
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1) #줄바꿈
print(t_s2)

#Raw String
raw_s1 = r'D:\python\test' # 앞에 r을 붙인다
print(raw_s1)

#멀티라인 입력
# \를 사용
multi_str = \
'''
String
Multi Line
Test
'''
print(multi_str)

multi_str2 = \
'dfsddsf' \
'dfddfd'
print(multi_str2)

#문자열 연산
str_o1 = "python"
str_o2 = 'Apple'
str_o3 = "How ard you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #시퀀스 str, list, tuple형은 in을 사용 할 수 있다
print('n' in str_o1)
print('P' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

#문자열 함수( upper, isalnum, startwith, count, endswith, isalpha ...)
print("Capitalize:", str_o1.capitalize()) #첫번째 시작글자를 대문자로
print("endswith?:", str_o2.endswith('e')) #마지막 글자 e로 끝나는지 검사
print("replace:", str_o1.replace('thon', ' Good')) #앞에 값을 찾아서 바꾼다
print("sorted:", sorted(str_o1))
print("split:", str_o4.split(" ")) #공백을 기준으로 분리함

#반복 (시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) #__iter__

#출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:11]) # 5 6 7 8 9 10
print(str_s1[5:]) # [5:11] 5부터 끝까지
print(str_s1[:len(str_s1)]) #str_s1[:11]
print(str_s1[:len(str_s1)-1]) #str_s1[:10]
print(str_s1[1:9:2]) # 8번째까지 가져오는데 2칸씩 점프
print(str_s1[-5:]) #-붙으면 꺼꾸로
print(str_s1[1:-2]) # ice Pyth
print(str_s1[::2]) #처음부터 끝까지 2칸씩 점프하면서 가져온다
print(str_s1[::-1]) #꺼꿀로 출력 (nohtyP eciN)

# 아스키코드(또는 유니코드)
a = 'z'
print(ord(a)) # z에 해당하는 아스키코드값은 122
print(chr(122)) # 아스키코드값을 문자로 출력
