import json

humanDict = {
    'age':20, 'name':'유현식', 'hobby':'독서', 
    'address': {'city':'seoul', 'gu':'마포구', 'zipcode':'12345'}
}

print(type(humanDict))
print(humanDict)

print('dumps 함수는 사전을 문자열 형식으로 변형해 줍니다.')
# ensure_ascii=False : 문자열을 이스케이프하지 않고, 한글을 그대로 보여 주고자 할 때 사용합니다.
humanString = json.dumps(humanDict, ensure_ascii=False, indent=4, sort_keys=True)
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)

print(f'이름 : {humanJson["name"]}')
print(f'취미 : {humanJson["hobby"]}')
print(f'나이 : {humanJson["age"]}')
print(f'시도 : {humanJson["address"]["city"]}')
print(f'군구 : {humanJson["address"]["gu"]}')
print(f'우편 번호 : {humanJson["address"]["zipcode"]}')