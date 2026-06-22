mylist = ['아메리카노','카페라떼']

print('# append 함수를 이용하여 마지막 위치에 요소를 추가합니다.')
mylist.append('에스프레소')
mylist.append('마키아또')
mylist.insert(2, '바닐라라떼')

# len(mylist)은 요소의 갯수를 알려 줍니다.
print(len(mylist))
print(mylist[len(mylist)-1]) # 마지막 요소 추출

# mylist.clear()

mylist.sort()
print('오름차순 정렬 :', mylist)

mylist.sort(reverse=True)
print('내림차순 정렬 :', mylist)

newlist = ['A', 'b', 'C', 'd']
newlist.sort()
print('오름차 정렬 :', newlist)

newlist.sort(key=str.lower)
print('소문자로 변경 후 정렬 :', newlist)

newlist.sort(key=str.lower, reverse= True)
print('소문자로 변경 후 역순 정렬 :', newlist)


print('reverse() 함수를 이용하여 순서 뒤집기')
mylist.reverse()
print(mylist)

mylist[2] = '카푸치노'

mylist.remove('카페라떼')

newlist = ['고구마라떼', '콜드브루', '아메리카노']
mylist.extend(newlist)

print(mylist.count('아메리카노'))

# '카푸치노'은 몆번째에 있나요? (힌트) index() 함수 사용
print('index :', mylist.index('카푸치노'))

print('index :', mylist.index('아메리카노', 4))

print(mylist)

print('\n# mylist는 타입에 구애 받지 않고, 무엇이든지 저장 가능합니다.')
anydata = [10, '가가', 12.34, [10, 20, 30]]
print(anydata)