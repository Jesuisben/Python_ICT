from xml.etree.ElementTree import parse

tree = parse(source='Car_Info.xml')

# xml 엘리먼트의 가장 바깥쪽 엘리먼트를 root 엘리먼트라고 합니다.
myroot = tree.getroot()
print(type(myroot))

carList = myroot.findall('car')
print(type(carList))
print('총 car 수 : %d' % len(carList))

# 차량 목록 정보를 tuple로 가지고 있는 list
car_list = []


for oneCar in carList:
    print('car 구성 정보')
    brand = oneCar[0].text
    brandName = oneCar[0].attrib['name']
    model = oneCar[1].text
    year = oneCar[2].text
    color = oneCar[3].text
    
    print('브랜드 : %s' % (brand))
    print('브랜드 이름 : %s' % (brandName))
    print('모델 : %s' % (model))
    print('제작 년도 : %s' % (year))
    print('색상 : %s' % (color))

    car_list.append((brand, brandName, model, color))

    print('-'*30)
# end for

print(car_list)