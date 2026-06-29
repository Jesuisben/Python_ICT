# XML 파일을 읽어서 트리로 파싱하는 parse함수를 가져옴
from xml.etree.ElementTree import parse

dataIn = "../dataIn/"
# parse("파일경로(이름)") : 해당 XML 파일을 읽어서 ElementTree 객체로 반환함
# ElementTree(xmldata).write()의 반대 방향이라고 생각하면 됨
tree = parse(source=dataIn + "XmlExam03.xml")

# getroot() : ElemenTree의 객체인 tree에서 루트 태그(최상위 Element)인 <가족들>을 Element 객체로 가져옴
myroot = tree.getroot()
# <class 'xml.etree.ElementTree.Element'>
print(type(myroot))

# findall("태그명") : 루트의 직계 자식 중 해당 태그명을 가진 것들을 "리스트"로 반환함
families = myroot.findall("가족")
# <class 'list'>
print(type(families))
# 총가족수 : 2
print("총가족수 : %d" % len(families))

# families : 리스트 타입
# family : ElementTree.Element 타입
# Element는 자식 (SubElement를 인덱스로 접근 가능)
for family in families:
    print("가족 구성원")

    # family는 "가족"인 SubElement
    for saram in family:
        # .tag는 태그 이름임 (문자열로 반환함)
        # .tag vs .text : .tag는 태그의 이름을 문자열로 반환 / .text는 태그 안에 있는 텍스트를 문자열로 반환
        tagName = saram.tag

        # len(saram) : saram이라는 부모 태그가 가지는 자식태그 갯수
        if len(saram) >= 1:
            # Element는 자식 (SubElement를 인덱스로 접근 가능)
            # .text : 태그 안의 텍스트를 문자열로 반환
            name = saram[0].text
            age = saram[1].text

            if tagName == "어머니":
                # attrib[""]로 saram태그의 자식인 saram[0]태그의 속성 가져오기
                info = saram[0].attrib["정보"]
                message = "태그명 : %s, 이름 : %s, 나이 : %s, 정보 : %s" % (tagName, name, age, info)
            else:
                message = "태그명 : %s, 이름 : %s, 나이 : %s" % (tagName, name, age)

            print(message)
        else:
            name = saram.attrib["이름"]
            age = saram.attrib["나이"]
            message = "태그명 : %s, 이름 : %s, 나이 : %s" % (tagName, name, age)
            print(message)