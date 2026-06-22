import re
from xml.etree.ElementTree import parse

tree = parse('shopList.xml')
shopRoot = tree.getroot()
print(type(shopRoot))

print('매장 개수 : %d' % len(shopRoot))

totalShop = [] # 전체 매장 정보 리스트

sidoDict = {} # 시도별 매장 집계 사전
gunguDict = {} # 군구별 매장 집계 사전

for store in shopRoot.iter('item'):
    onestore = [] # 매장 1개 정보(상호명, 주소, 전화번호)
    onestore.append(store.find('aname1').text)

    address01 = store.find('aname4').text
    # print(address01)

    imsi = store.find('aname5').text

    regex = '\d\S*'
    pattern = re.compile(regex)
    mysearch = pattern.search(imsi)
    address02 = mysearch.group()

    # 세부 주소에 '번길'이나 '번지'라는 글자가 있으면 한칸 띄웁시다.
    # 변경할 단어가 많으면, list와 for 구문을 사용하셔야 합니다.
    # 간단한 내용이라서 replace 함수를 사용하지만, 정규식 sub() 함수도 생각해 보셔야 합니다.
    address02 = address02.replace('번길', '번길 ')
    address02 = address02.replace('번지', '번지 ')
    # print(type(address02))
    # print(address02)
    address = address01 + ' ' + address02
    onestore.append(address)

    phone = store.find('aname7').text
    regex = '-'
    pattern = re.compile(regex)
    phone = pattern.sub('/', phone)

    onestore.append(phone)

    totalShop.append(onestore)

    # print('시도별 매장 개수를 집계합니다.')
    sido = store.find('aname2').text

    if sido in sidoDict:
        sidoDict[sido] = sidoDict[sido] + 1
    else:
        sidoDict[sido] = 1
    # end if

    # print('군구별 매장 개수를 집계합니다.')
    gungu = store.find('aname3').text

    if gungu in gunguDict:
        gunguDict[gungu] = gunguDict[gungu] + 1
    else:
        gunguDict[gungu] = 1
    # end if
# end for

print(totalShop)
print('시도별 매장 집계 :\n', sidoDict)
print('군구별 매장 집계 :\n', gunguDict)
