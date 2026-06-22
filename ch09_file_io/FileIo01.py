# FileIo01.py
# mode는 읽기(read)/덮어 쓰기(write)/추가(append) 모드
print('파일에 기록합니다.')
filename = 'newfile.txt'
myfile01 = open(file=filename, mode='wt', encoding='UTF-8')
print(type(myfile01))

members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    message = f'\'{mem}\'님 안녕하세요.\n'
    myfile01.write(message)
# end for

myfile01.close()
print(f'{filename} 파일이 생성됨' )


print('기존 파일에 내용을 추가합니다.') # at = append text
myfile02 = open(file=filename, mode='at', encoding='UTF-8')

# 홀수 번째 고객님과 짝수 번째 고객님에 대한 멘트를 다르게 적용해 보기
for idx in range(len(members)):
    if idx % 2 == 0:
        message = f'{idx}번째 고객 {members[idx]}님 방가워요.\n'
    else:
        message = f'{idx}번째 고객 {members[idx]}님 어서오세요.\n'
    # end if

    myfile02.write(message)
# end for

myfile02.close()

print('반복문을 사용하여 파일을 여러개 만들어 봅니다.')
print('파일 이름 : somefile01.txt ~ somefile10.txt')
for idx in range(1, 11):
    filename = 'somefile' + str(idx).zfill(2) + '.txt'
    # print(filename)
    myfile = open(file=filename, mode='wt', encoding='UTF-8')
    myfile.write(f'나는 "{filename}" 파일입니다.\n')
    myfile.close()
# end for

print('다음 멤버들의 이름을 사용하여 파일로 만들어 보세요.')
# 예시 : '홍영식.txt', '김민수.txt' 등등
members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    filename = mem + '.txt'
    myfile = open(file=filename, mode='wt', encoding='UTF-8')
    myfile.write(mem + ' 고객을 위한 텍스트 파일입니다.\n')
    myfile.close()
# end for

print('with 구문을 사용하면, close() 함수를 사용하지 않아도 자동으로 closing 동작을 수행합니다')
with open(file='test.txt', mode='wt', encoding='UTF-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')
    
    # file 매개 변수를 변경하여 testfile 파일에 출력하겠습니다.
    print('hello~world', file=testfile)
# end with    
# with 구문은 암시적으로 close() 함수를 호출합니다.

print('finished')
