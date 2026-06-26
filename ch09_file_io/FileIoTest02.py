dataIn = "../dataIn/"

filename = 'coffee_list.txt'

coffees = ['아메리카노', '라떼', '카푸치노', '바닐라라떼', '모카']

with open(file=dataIn + filename, mode="w", encoding="UTF-8") as myfile01:
    for item in coffees:
        myfile01.write(f"{item}\n")

# readline() 함수는 1줄을 읽어 옵니다.
with open(file=dataIn + filename, mode="r", encoding="UTF-8") as myfile02:
    print(myfile02.readline().strip())

# readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.
with open(file=dataIn + filename, mode="r", encoding="UTF-8") as myfile03:
    coffees = [item.strip() for item in myfile03.readlines()]
    print(coffees)


# read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.
with open(file=dataIn + filename, mode="r", encoding="UTF-8") as myfile04:
    print(myfile04.read())