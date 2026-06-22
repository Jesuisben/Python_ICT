coffee = 3
price = 2000

print('판매 가능한 커피 잔량 : %d' % coffee)
print('단가 : %d원' % price)

while True:
    money = int(input('돈을 넣어 주세요 : '))
    if money > price:
        change = money - price
        print('커피 %d잔 판매, 거스름돈 : %d원' % (1, change))
        coffee -= 1
    elif money == price:
        print('커피 %d잔 판매' % (1))
        coffee -= 1
    else:
        print('돈이 부족하여 판매가 불가능합니다.')
    # end if

    print('남은 잔수 : {}잔'.format(coffee))

    if coffee == 0:
        print('더 이상 판매할 커피가 없어서 프로그램을 종료합니다.')
        break # 진행중인 반복문을 강제 종료시 사용하는 키워드
# end while