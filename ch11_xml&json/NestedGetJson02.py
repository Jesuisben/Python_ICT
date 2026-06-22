import json

filename = 'nestedHumanData.json'

# Unexpected UTF-8 BOM (decode using utf-8-sig):
myfile = open(filename, 'rt', encoding='UTF-8')
mystring = myfile.read()
jsondata = json.loads(mystring)
print(type(jsondata))
print('요소 개수 : %d' % len(jsondata))
print()
for id in jsondata:
    print('id : %s' % id)
    name = jsondata[id]['name']
    age = jsondata[id]['age']

    street = jsondata[id]['address']['street']
    city = jsondata[id]['address']['city']
    gu = jsondata[id]['address']['gu']

    print('이름 : %s' % name)
    print('나이 : %d' % age)
    print('도로명 : %s' % street)
    print('시도 : %s' % city)
    print('군구 : %s' % gu)
    print()
# end for