from xml.etree.ElementTree import parse

tree = parse(source='xmlEx_03.xml')

# xml 엘리먼트의 가장 바깥쪽 엘리먼트를 root 엘리먼트라고 합니다.
myroot = tree.getroot()
print(type(myroot))

families = myroot.findall('가족') # 여러 가족들
print(type(families))
print('총 가족 수 : %d' % len(families))

for family in families:
    print('가족 구성 정보')
    # family : 1가족
    for saram in family:
        tagName = saram.tag
        if len(saram) >= 1: # 하위 엘리먼트가 있으면
            name = saram[0].text
            age = saram[1].text

            if tagName == '어머니':
                info = saram[0].attrib['정보']
                message = '태그명 : %s, 이름 : %s, 나이 : %s, 정보 : %s' % (tagName, name, age, info)
            else :
                message = '태그명 : %s, 이름 : %s, 나이 : %s' % (tagName, name, age)
            # end if
            print(message)

            if len(saram) == 3:
                blood = saram[2].text
                print('%s의 혈액형 : %s' % (tagName, blood))
            # end if
        else:
            name = saram.attrib['이름']
            age = saram.attrib['나이']
            message = '태그명 : %s, 이름 : %s, 나이 : %s' % (tagName, name, age)
            print(message)
    print()
# end for