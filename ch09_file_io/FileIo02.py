# FileIo02.py
filename = 'test.txt'
myencoding = 'UTF-8'

print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file=filename, mode='r', encoding=myencoding)
while True:
    oneline = myfile01.readline().strip()

    # 파이썬에서 empty한 데이터는 부정(False)으로 취급합니다.
    # 마지막에는 빈 문자열이므로 부정(False)입니다.
    if not oneline:
        print(type(oneline))
        print('[' + oneline + ']')
        break
    print('[' + oneline + ']')

myfile01.close()


print('readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file=filename, mode='r', encoding=myencoding)
sentences = [txt.strip() for txt in myfile02.readlines()]
print(sentences)
myfile02.close()


print('read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')
myfile03 = open(file=filename, mode='r', encoding=myencoding)
sentences = myfile03.read()
print(type(sentences))
print(sentences)
myfile03.close()