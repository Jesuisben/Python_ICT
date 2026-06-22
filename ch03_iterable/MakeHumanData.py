humanDict = dict()

while True:
    name = input('이름 입력 : ')
    if name == 'quit':
        print('while 구문을 종료합니다.')
        break

    age = int(input('나이 입력 : '))
    humanDict[name] = age

print(humanDict)