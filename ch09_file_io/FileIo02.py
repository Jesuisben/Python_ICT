dataIn = "../dataIn/"

# FileIo02.py
filename = dataIn + 'test.txt'
myencoding = 'UTF-8'

# readline() : 1줄 읽어오는 함수 / 반환타입 : 문자열
print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file=filename, mode='r', encoding=myencoding)
while True:
    # 문자열에 보이지 않는 화이트 캐릭터인 \n(줄바꿈)를 없애려고 .strip() 사용
    # myfile01.readline() : 내부적으로 \n이 있는 곳까지 파일 포인터가 가서 그 부분까지 출력함
    # 파일이 열리고 파일이 닫힐때까지 파일 포인터가 파일 내부에 존재를 해서
    # 어디까지 이 함수로 파일의 영역을 사용했는지 알려줌
    # 그래서 myfile01.readline()를 쓰면 자동으로 파일 포인터가 움직여서
    # myfile01.readline() 이 함수를 2번쓰면 자동으로 2번째 줄을 읽어오는 것임
    # 이 파일 포인터는 파일이 닫히면 사라지기에 파일을 닫고 다시 열면 초기화된 상태여서
    # 파일을 닫고 다시 열고 myfile01.readline() 이 함수를 다시 실행하면 첫번째 줄부터 읽어옴
    oneline = myfile01.readline().strip()

    # 리액트에 나왔던 falsy, truthy 개념과 비슷
    # Falsy : False, 0, "", [], {}, None 등
    # Truthy : True, 1, "문자열", [1,2,3], {"a":1} 등 값이 있으면
    # 파이썬에서 empty한 데이터는 부정(False)으로 취급합니다.
    # 마지막에는 빈 문자열이므로 부정(False)입니다.
    if not oneline: # 문서의 끝까지 갔다면
        print(type(oneline))
        print('[' + oneline + ']')
        break
    print('[' + oneline + ']')

myfile01.close()

# readlines() : 여러줄을 한줄씩 읽어오는 함수 / 반환타입 : List
print('readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file=filename, mode='r', encoding=myencoding)
# .readlines()로 가져와도 \n이 포함되어있어서 .strip() 사용함
sentences = [txt.strip() for txt in myfile02.readlines()]
print(sentences)
myfile02.close()

# read() : 내용 전체를 읽어오는 함수 / 반환타입 : 문자열
print('read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')
myfile03 = open(file=filename, mode='r', encoding=myencoding)
sentences = myfile03.read()
print(type(sentences))
print(sentences)
myfile03.close()