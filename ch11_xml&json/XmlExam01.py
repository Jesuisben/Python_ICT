from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import SubElement

# human 엘리먼트를 생성하면서, gender 속성도 같이 추가합니다.
xmldata = Element('human', gender="남자")

# 기존 엘리먼트에 속성 추가하기
xmldata.attrib['birth'] = '19951225'

SubElement(xmldata, 'name').text = '홍길동'
SubElement(xmldata, 'age').text = '30'
SubElement(xmldata, 'address').text = '마포구 공덕동'

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

xmlFile = 'xmlEx_01.xml'
ElementTree(xmldata).write(xmlFile, encoding='UTF-8')
print(xmlFile + '파일이 생성되었습니다.')