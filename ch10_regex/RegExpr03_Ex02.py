import re

'''
문제) 아이디 가져 오기
첨부 파일 myid.txt에 들어 있는 데이터를 읽어 들여서, id를 추출하는 프로그램을 작성해 보세요.
단, id는 소괄호 '('와 ')' 사이에 들어 있는 문자열을 의미합니다.
정규식 소괄호 기호는 특수 문자라서 '\('와 '\)' 의 형식으로 작성해야 합니다.
'''
myfile = open(file='myid.txt', mode='rt', encoding='utf-8')

mylist = [item.strip()  for item in myfile.readlines()]
print(mylist)

myfile.close()

for item in mylist:
    # 소괄호 () 안에 공백이 포함되지 않은 문자열을 찾는 정규식입니다.
    regex = '\(\S+\)' # 소괄호와 대괄호 사이에 있는 non white character 문자열
    pattern = re.compile(regex)
    popdata = pattern.search(item)

    # print(popdata)
    if (popdata != None):
        result = str(popdata.group())
        print(result.replace('(', '').replace(')', ''))
    # end if
# end for

# 출력 결과
# world
# hello