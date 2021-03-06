# File Write
# 파일 읽기 및 쓰기
# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a || 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로 ('../, ./'), 절대 경로 ('C:\Django\example..')

# 파일 읽기(Read)
f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # 텍스트로 읽을경우 : r or rt, 바이너리로 읽을경우 : rb
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 파일 내용읽기
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제 2
# with 내부적으로 커넥션을 반납한다 (close 호출할 필요 없음)
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    
print()

# 예제3
# read() : 전체 읽기, read(10) : 10 Byte 
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20) #커서가 이동한다.
    print(c) #Right now gamers can
    c = f.read(20) 
    print(c) # pay just $1 for acc
    c = f.read(20) 
    print(c) #ess to hundreds of t
    f.seek(0, 0) # 처음으로 커서를 되돌린다
    c = f.read(20) 
    print(c) #Right now gamers can
print()

# 예제4
# readline() : 한줄씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.readline() # 한줄씩 읽는다
    print(c)
    c = f.readline() # 한줄씩 읽는다
    print(c)
print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines() 
    print(cts)
    print()
    for c in cts:
        print(c, end='')
print()

# 파일 쓰기(write)
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)