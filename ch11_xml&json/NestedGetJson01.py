import json

filename = 'some.json'

# Unexpected UTF-8 BOM (decode using utf-8-sig):
myfile = open(filename, 'rt', encoding='UTF-8')
mystring = myfile.read()
jsondata = json.loads(mystring)
print(type(jsondata))
print(jsondata)

name = jsondata['member']['name']
address = jsondata['member']['address']
phone = jsondata['member']['phone']

print('이름 : ' + name)
print('주소 : ' + address)
print('전화 번호 : ' + phone)

# 웹 페이지 정보 출력해 보세요.
cafename = jsondata['web']['cafename']
id = jsondata['web']['id']

print('cafename : ' + cafename)
print('아이디 : ' + id)