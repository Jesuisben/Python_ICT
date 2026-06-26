# 1) 요구 사항
# 할인율 사전 정보를 이용하여 단 제품의 판매 금액을 구하여 다음과 같이 처리하세요.
# 할인율에 해당 key의 정보가 존재하지 않으면, 기본 할인율 0.06을 적용하도록 합니다.

# 2) 읽어올 파일 (생성)
# coffee.txt 파일 내용
#
# 아메리카노,1000,10
# 라떼,1500,5
# 카푸치노,2000,3
# 바닐라라떼,2500,2
# 모카,3000,4

# 4) 할인율
discounts = {
	"아메리카노": 0.10, 	# 10% 할인
	"라떼": 0.05, 			# 5% 할인
	"카푸치노": 0.07, 	# 7% 할인
	"바닐라라떼": 0.08, 	# 8% 할인
}

dataIn = "../dataIn/"
dataOut = "../dataOut/"

filename = 'coffee.txt'

coffee_new_list = []

with open(file=dataIn + filename, mode="r", encoding="UTF-8") as myfile01:
    coffee_list = [item.strip().split(",") for item in myfile01.readlines()]
    print(coffee_list)
    for coffee in coffee_list:
        try:
            coffee_disc = int((int(coffee[1]) * int(coffee[2])) - (int(coffee[1]) * int(coffee[2])) * discounts[f"{coffee[0]}"])
        except KeyError:
            coffee_disc = int((int(coffee[1]) * int(coffee[2])) - ((int(coffee[1]) * int(coffee[2])) * 0.06))

        coffee_new_list.append(f"{coffee[0]}/{coffee[1]}/{coffee[2]}/{coffee_disc}")

# 3) 생성될 파일
with open(file=dataOut + "coffee_result.txt", mode="w", encoding="UTF-8") as myfile02:
    for result in coffee_new_list:
        myfile02.write(f"{result}\n")