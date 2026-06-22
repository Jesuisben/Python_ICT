from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import SubElement

# 다음 사전 정보를 이용하여 xml 파일을 생성해 보세요.
humanDict = {'kim': ('김철수', 30, '남자', '마포구 공덕동'), 'park': ('박영희', 20, '여자', '동대문구 휘경동')}

print(humanDict)

# xml의 속성에 추가할 사전 정보
anotherDict = {'kim': ('01011112222', 'hello@naver.com'), 'park': ('01033334444', 'world@daum.net')}

xmldata = Element('members')

for key, mytuple in humanDict.items():
    mem = SubElement(xmldata, 'member')
    mem.attrib['id'] = key

    # 하위 엘리먼트 추가하기
    SubElement(mem, 'name').text = mytuple[0]
    SubElement(mem, 'age').text = str(mytuple[1])
    SubElement(mem, 'gender').text = mytuple[2]
    SubElement(mem, 'address').text = mytuple[3]

    # 튜플(전화 번호와 이메일 정보)를 사용하여 속성에 추가합니다.
    anotherInfo = anotherDict[key]
    mem.attrib['phone'] = anotherInfo[0]
    mem.attrib['email'] = anotherInfo[1]
# end for

def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# end def

indent(xmldata)

xmlFile = 'xmlExam02.xml'
ElementTree(xmldata).write(xmlFile, encoding='UTF-8')
print(xmlFile + '파일이 생성되었습니다.')
