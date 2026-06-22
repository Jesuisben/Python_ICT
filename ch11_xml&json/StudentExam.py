from xml.etree.ElementTree import parse

tree = parse('mystudent.xml')
myroot = tree.getroot()
# print(type(myroot))

totallist = []  #
for onesaram in myroot.iter('student'):
    # print(onesaram)
    sublist = []
    sublist.append(onesaram.find('name').text)
    sublist.append(float(onesaram.find('국어').text))
    sublist.append(float(onesaram.find('영어').text))
    sublist.append(float(onesaram.find('수학').text))
    totallist.append(sublist)
# end for
print( totallist)