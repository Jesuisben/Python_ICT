# SortedTest02.py
# sorted 함수는 iterable 객체를 정렬하여 새로운 list를 반환해 줍니다.

# 다음 항목을 오름차순 정렬해 보세요.
coffees = ['아메리카노', '카페라떼', '카푸치노', '디카페인커피']
result = sorted(coffees)
print(type(result))
print(result)

# 문자열의 길이로 정렬합니다.
# key : 정렬 기준 (len : 문자열 길이)
# reverse : 내림차순 여부 (True : 내림차순 O) <-> False
result = sorted(coffees, key=len, reverse=True)
print(result)

# 다음 항목을 내림차순 정렬해 보세요.
# key(정렬기준)를 정하지 않으면 기본값은 알파벳/유니코드 순서임
result = sorted(coffees, reverse=True)
print(result)

# 정렬된 결과를 사전으로 만들어 보세요.
coffeeDict = {}
# enumerate는 차후에 설명함
for qty, name in enumerate(result, start=1):
    coffeeDict[name] = 10 * qty

print(coffeeDict)

# 다음 성적 정보에서 key를 사용하여 오름차순, 내림차순 정렬해 보세요.
# value를 사용하여 오름차순, 내림차순 정렬해 보세요.
# 고득점자부터 명단을 출력해 보세요
sungjuk = {'강효진': 60, '김윤지': 30, '신민정': 20, '이지환': 50}

print('key를 사용한 오름차순 정렬')
result = sorted(sungjuk.keys())
print(result)

print('key를 사용한 내림차순 정렬')
result = sorted(sungjuk.keys(), reverse=True)
print(result)

print('value를 사용한 오름차순 정렬')
result = sorted(sungjuk.values())
print(result)

print('value를 사용한 내림차순 정렬')
result = sorted(sungjuk.values(), reverse=True)
print(result)

print('고득점자부터 출력하기')
# 점수가 높은 사람부터 정렬하되, 이름을 읽어 들입니다.
# key=sungjuk.get : 해당하는 key의 value를 기준으로 정렬
# 원리 : 내부적으로 sungjuk.get(key값)을 순회해서 서로 크기 비교를 해서 기분을 세움
result = sorted(sungjuk, key=sungjuk.get, reverse=True)
print(result)