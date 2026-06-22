from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import SubElement

xmldata = Element('student', address="상수동")

xmldata.attrib['birth'] = '19951225'

SubElement(xmldata, 'name').text = '김대호'
SubElement(xmldata, 'age').text = '20'
SubElement(xmldata, 'gender').text = '남자'
SubElement(xmldata, 'grade').text = 'A'
SubElement(xmldata, 'university').text = '서강대'

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

xmlFile = 'XmlTest_01.xml'
ElementTree(xmldata).write(xmlFile, encoding='UTF-8')
print(xmlFile + '파일이 생성되었습니다.')