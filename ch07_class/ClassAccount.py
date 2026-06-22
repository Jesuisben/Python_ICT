class Account:
    bankname = 'KB'  # 클래스 변수

    def __init__(self, name, no, deposit):
        # 인스턴스 변수
        self.name = name
        self.no = no
        self.deposit = deposit

    def printData(self):
        print('예금주 : %s' % (self.name))
        print('계좌 번호 : %d' % (self.no))
        print('예치금 : %d' % (self.deposit))


print('거래처 : %s' % (Account.bankname))
print('-' * 20)

soo = Account('김철수', 1234, 1000)
soo.printData()

print('-' * 20)

hee = Account('박영희', 5678, 2000)
hee.printData()
