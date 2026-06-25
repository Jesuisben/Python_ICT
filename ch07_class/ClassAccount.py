# 클래스 생성
class Account :
    # 클래스에 변수 하나 생성
    # 클래스 변수라고 부름 (static 변수)
    bankname = "KB"

    # 생성자 만들기
    # 1. self 설명
    # self를 매개변수에 적지만 기본으로 적는 것이기에
    # 매개변수 갯수에 영향을 주지는 않음 (그냥 생성자라는 표시 느낌??)
    # 따라서 생성자에 지정할 매개변수는 self 이후에 적으면 됨
    # 2. 자바와의 차이점
    # (중요!!) 맴버변수를 미리 클래스에 선언하지 않고 클래스 내부의 생성자 내부에서 바로 생성함
    # -> 클래스 내부에 생성한 변수는 클래스 변수이고 자바의 static 변수와 같다.
    # (중요!!) 매개변수가 다른 생성자를 여러개 만들 수 없음 (오버로딩 할 수 없음)
    # -> 매개변수에 기본값을 넣는 등 우회해서 사용하긴 함
    def __init__(self, name, no, deposit): # 매개변수 name, no, deposit인 생성자
        # self.name : 맴버 변수 / name : 매개변수
        # self는 자바의 this.와 같음
        self.name = name
        self.no = no
        self.deposit = deposit

    # 맴버 메소드
    # 생성자를 포함해서 클래스 내부에 있는 모든 메소드는 매개변수로 self를 가져야 함
    # 이유 : soo 객체를 이용해서 soo.print_data() 를 호출 Python이 내부적으로
    # Account.print_data(soo) -> 이렇게 작동함 (soo를 자동으로 첫번째 매개변수로 넘김)
    # self가 없으면 매개변수를 받을 매개변수가 없어서 에러가 남
    def print_data(self):
        print("예금주 : %s" % self.name)
        print("계좌 번호 : %s" % self.no)
        print("예치금 : %s" % self.deposit)

# 클래스의 클래스 변수를 객체 없이 직접 호출
# (마치 자바의 static 변수 느낌)
# 문법 : 클래스명.클래스변수명
print("거래처 : %s" % Account.bankname)

# 생성한 클래스를 이용한 객체 생성
# soo : 객체명 / Account() : 생성자

# 파이썬에서도 자바처럼 기본 생성자가 존재함 (눈에 안보이지만)
# 생성자를 정의할때 : 자바는 생성자명과 클래스명이 동일 / 파이썬은 생성자명이 __init__으로 고정됨
# 생성자를 호출할때 : 자바와 같이 생성자명이 클래스명과 같아야함
soo = Account("김철수", 1234, 1000) # 예금주, 계좌번호, 예치금

soo.print_data()

print(type(soo))

print("-"*20)

hee = Account("박영희", 5678,2000)
hee.print_data()




















# class Account:
#     bankname = 'KB'  # 클래스 변수
#
#     def __init__(self, name, no, deposit):
#         # 인스턴스 변수
#         self.name = name
#         self.no = no
#         self.deposit = deposit
#
#     def printData(self):
#         print('예금주 : %s' % (self.name))
#         print('계좌 번호 : %d' % (self.no))
#         print('예치금 : %d' % (self.deposit))
#
#
# print('거래처 : %s' % (Account.bankname))
# print('-' * 20)
#
# soo = Account('김철수', 1234, 1000)
# soo.printData()
#
# print('-' * 20)
#
# hee = Account('박영희', 5678, 2000)
# hee.printData()
