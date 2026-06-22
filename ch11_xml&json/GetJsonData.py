import json

filename = 'jumsu.json'

# t(기본값_텍스트 파일), b(그림 파일)
myfile = open(file=filename, mode='rt', encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

print('loads 함수는 문자열을 읽어서 dict을 원소로 담고 있는 list를 변환해 줍니다.')
jsonData = json.loads(mystring)
print(type(jsonData)) # list 타입

# 학생들의 정보를 tuple 형식으로 담고 있는 list
humanList = list()

for human in jsonData:
    name = human['name']
    print('이름 : %s' % name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    if 'hello' in human.keys():
        message = human['hello']
        print('메시지 : ', message)
    else:    
        message = '냉무'
    # end if

    _gender = human['gender'].upper()

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    # end if
    
    mytuple = (name, kor, eng, math, total, gender, message)
    humanList.append(mytuple)
# end for

print(humanList)