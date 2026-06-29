# Python 표준 라이브러리의 XML 모듈에서 3개를 가져옴
# Element : XML 태그 하나
# SubElement : 자식 태그
# ElementTree : XML 파일 전체 트리 (파일 저장용)
from xml.etree.ElementTree import Element, ElementTree, SubElement

# Element() : Element 생성시 태그를 넣고 바로 속성을 넣을 수 있음
# xmldata : Element 객체임
xmldata = Element("human", gender="남자")
# attrib["키"] = "값" : Element의 속성을 담는 딕셔너리
# Element 생성 이후 딕셔너리에 키-값을 추가하듯이 속성을 추가할 수 있음
xmldata.attrib["birth"] = '20001225'

# SubElement(부모태그, 자식태그) : 자식태그에 자신의 이름을 넣고 .text로 바로 태그 안 텍스트를 작성 가능
SubElement(xmldata, "name").text = "홍길동"
SubElement(xmldata, "age").text = "30"
SubElement(xmldata, "address").text = "마포구 공덕동"

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

# 줄맞춤 하는 함수
indent(xmldata)

dataOut = "../dataOut/"

xml_file = dataOut + "xml_01.xml"
# ElementTree(xmldata) 로 트리를 만들고 .write()로 파일에 저장
# Element 객체인 xmldata를 ElementTree()에 넣어서 파일로 저장 가능한 트리 객체로 반환함
# write(파일경로(이름), 인코딩_방식) : 트리 객체의 메소드, 실제 파일이 생성됨
ElementTree(xmldata).write(xml_file, encoding="UTF-8")
print(xml_file + "생성 완료")


# from xml.etree.ElementTree import Element, ElementTree

# from xml.etree.ElementTree import SubElement
#
# # human 엘리먼트를 생성하면서, gender 속성도 같이 추가합니다.
# xmldata = Element('human', gender="남자")
#
# # 기존 엘리먼트에 속성 추가하기
# xmldata.attrib['birth'] = '19951225'
#
# SubElement(xmldata, 'name').text = '홍길동'
# SubElement(xmldata, 'age').text = '30'
# SubElement(xmldata, 'address').text = '마포구 공덕동'
#
# def indent(elem, level=0):
#     mytab = '\t'
#     i = '\n' + level * mytab
#
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text = i + mytab
#
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#
#         for elem in elem:
#             indent(elem, level + 1)
#
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = i
# # end def
#
# indent(xmldata)
#
# xmlFile = 'xmlEx_01.xml'
# ElementTree(xmldata).write(xmlFile, encoding='UTF-8')
# print(xmlFile + '파일이 생성되었습니다.')