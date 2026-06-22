class Fruit:
    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price

    def showInfo(self, cnt):
        print('%d번째 품목 : %s' % (cnt, self.item))
        print('수량 :', self.qty)
        print('단가 :', self.price)

        amount = (1 - 0.1) * self.qty *self.price
        print('판매 금액 : %.3f' % (amount))
# end class Fruit:

class Sales:
    def __init__(self, iter):
        totalsum = 0
        for idx in range(iter):
            item = input('품목 입력 : ')
            qty = int(input('수량 입력 : '))
            price = int(input('단가 입력 : '))
            self.fruit = Fruit(item, qty, price)
            self.fruit.showInfo(idx+1)
            totalsum += qty
        # end for

        print('총 판매 수량 : ', totalsum)

iter = 2 # 상품 판매 건수
mysales = Sales(iter)