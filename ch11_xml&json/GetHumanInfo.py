import json

filename = 'humans.json'

myfile = open(file=filename, mode='rt', encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

print('loads 함수는 문자열을 읽어서 dict 타입으로 변환해 줍니다.')
jsonData = json.loads(mystring)
print(type(jsonData)) # list 타입

humanList = list()

for human in jsonData:
    name = human['name']
    hobby = human['hobby']
    address = human['address']
    blood = human['blood'] + '형'
    ssn = human['ssn']

    if int(ssn[0:2]) >= 50:# 1900년대 생일
        gen = 1900 + int(ssn[0:2])
    else:
        gen = 2000 + int(ssn[0:2])
    # end if

    age = 2024 - gen
    gender = '남자' if ssn[7] in ['1', '3'] else '여자'

    mytuple = (name, age, address, hobby, ssn, gender, blood)
    humanList.append(mytuple)
# end for

print(humanList)