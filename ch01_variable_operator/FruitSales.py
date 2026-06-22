# 출력 내용
"""
구매 정보
사과 3개 구매, 가격 : 3000
감 10개 구매, 가격 : 5000

결재 정보
내신 금액 : 10000
잔돈 : 2000
"""

appleQty = 3
gamQty = 10

applePrice = 1000
gamPrice = 500

money = 10000
change = money - (applePrice * appleQty + gamPrice * gamQty)

# print('사과 {}개 구매, 가격 :{}'.format(appleQty, applePrice * appleQty))
# print('감 {}개 구매, 가격 :{}'.format(gamQty, gamPrice * gamQty))
# print('내신 금액 : %d' % (money))
# print('잔돈 : %d' % (change))


print("# 하드 코딩")
print("구매 정보")
print("사과 {}개 구매, 가격 : {}".format(appleQty, (appleQty * applePrice)))
print("감 {}개 구매, 가격 : {}".format(gamQty, (gamQty * gamPrice)))
print("")
print("결재 정보")
print("내신 금액 : {}".format((appleQty * applePrice) + (gamQty * gamPrice)))
print("잔돈 : {}".format(money - ((appleQty * applePrice) + (gamQty * gamPrice))))

print("")

print("# 변수 생성 후 이용")
appleQtyPrice = appleQty * applePrice # 사과 최종가격
gamQtyPrice = gamQty * gamPrice # 감 최종가격
totalPrice = appleQtyPrice + gamQtyPrice # 최종 지불 가격
leftMoney = money - totalPrice
print("구매 정보")
print("사과 {}개 구매, 가격 : {}".format(appleQty, appleQtyPrice))
print("감 {}개 구매, 가격 : {}".format(gamQty, gamQtyPrice))
print("")
print("결재 정보")
print("내신 금액 : {}".format(totalPrice))
print("잔돈 : {}".format(leftMoney))