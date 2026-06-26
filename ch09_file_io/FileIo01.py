# FileIo01.py
# mode는 읽기(read)/덮어 쓰기(write)/추가(append) 모드
dataIn = "../dataIn/"

print('파일에 기록합니다.')
filename = dataIn + 'newfile.txt'
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

# 한개의 파일 생성
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

# 여러개의 파일 생성
# 반복문 안에 open()과 close()를 넣어줘야함 (중요!)
print('반복문을 사용하여 파일을 여러개 만들어 봅니다.')
print('파일 이름 : somefile01.txt ~ somefile10.txt')
for idx in range(1, 11):
    filename = dataIn + 'somefile' + str(idx).zfill(2) + '.txt'
    # print(filename)
    myfile = open(file=filename, mode='wt', encoding='UTF-8')
    myfile.write(f'나는 "{filename}" 파일입니다.\n')
    myfile.close()
# end for

print('다음 멤버들의 이름을 사용하여 파일로 만들어 보세요.')
# 예시 : '홍영식.txt', '김민수.txt' 등등
members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    filename = dataIn + mem + '.txt'
    myfile = open(file=filename, mode='wt', encoding='UTF-8')
    myfile.write(mem + ' 고객을 위한 텍스트 파일입니다.\n')
    myfile.close()
# end for

# with 구문을 이용하여 close() 함수없이 파일 작업 끝내기
print('with 구문을 사용하면, close() 함수를 사용하지 않아도 자동으로 closing 동작을 수행합니다')
with open(file= dataIn + 'test.txt', mode='wt', encoding='UTF-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    # file 매개 변수를 변경하여 testfile 파일에 출력하겠습니다.
    # 원래 print() 함수는 콘솔창에 출력함
    print('hello~world')
    # file 매개변수를 이용해서 출력 위치를 다르게 지정할 수 있음
    # print의 매개변수 문자열을 file에 기록하게 코드를 작성함
    print('hello~world', file=testfile)
# end with
# with 구문은 암시적으로 close() 함수를 호출합니다.

print('finished')

# 추가로 writelines() 함수는 \n이 포함된 문자열의 컬렉션의 경우에 줄 단위로 기록이 가능함