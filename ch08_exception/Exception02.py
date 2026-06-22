menu = ['아메리카노', '라떼', '카푸치노', '바닐라라떼', '모카']

# 주문할 품목
orderList = ['아메리카노', '핫초코']

def coffeeCheck(order):
    if order not in menu:
        raise ValueError(f"'{order}'은(는) 판매하지 않는 메뉴입니다.")
    return f"{order} 주문이 완료되었습니다."

for item in orderList:
    try:
        print(coffeeCheck(item))
    except ValueError as e:
        print(e)