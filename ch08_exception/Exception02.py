menu = ["아메리카노", "라떼", "카푸치노", "바닐라라떼", "모카"]

order_list = ["아메리카노", "핫초코"]

def order_menu(product):
    if product not in menu:
        # 1. raise : 개발자가 의도적으로 예외 발생을 시키고자 할 때 사용
        # 의도적으로 예외를 발생을 시켜야 이 함수가 들어간 try문에서 에러가 나오고
        # 그 에러가 나와야 try-except문에서 except문으로 가서 예외 처리를 하기 때문에
        # 2. 없는 메뉴를 주문하는 것은 원래 코드상 오류가 아니지만
        # 실제에서는 오류이기에 그 오류에 대한 예외 처리
        # 3. Java의 throw같은 느낌 (throw new IllegalArgumentException("메시지");)
        # 4. raise로 직접 예외를 던질때는 메시지가 없는게 기본값이라서
        # 개발자가 직접 넣어줘야 함
        raise ValueError(f"'{product}'은(는) 판매하지 않습니다.")
    return f"{product} 상품 주문이 완료되었습니다."

# 주문할 리스트 요소가 메뉴 리스트에 존재하는 요소인지 체크
for item in order_list:
    try:
        print(order_menu(item))
    except ValueError as err:
        print(err)


# menu = ['아메리카노', '라떼', '카푸치노', '바닐라라떼', '모카']
#
# # 주문할 품목
# orderList = ['아메리카노', '핫초코']
#
# def coffeeCheck(order):
#     if order not in menu:
#         raise ValueError(f"'{order}'은(는) 판매하지 않는 메뉴입니다.")
#     return f"{order} 주문이 완료되었습니다."
#
# for item in orderList:
#     try:
#         print(coffeeCheck(item))
#     except ValueError as e:
#         print(e)