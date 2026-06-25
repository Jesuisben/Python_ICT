# Bag 클래스는 Dosirak 클래스를 포함
# Bag가 Dosirak을 가지고 있는 구조 (Has A)
# -> Bag Has A Dosirak
class Bag:
    isOpened = False   # 도시락 가방 문 개폐 여부 확인용
    dosirak = [] # Dosirak type 자료 저장용

    def open(self):
        self.isOpened = True
        print('# 도시락 가방 열기')

    def put(self, thing):
        if self.isOpened:
            self.dosirak.append(thing)   #포함
            print('# 도시락 가방에 도시락을 담음')
            self.list()
        else:
            print('# 도시락 가방이 닫혀서 도시락을 넣을 수 없음')

    def close(self):
        self.isOpened = False
        print('# 도시락 가방 닫기')

    def list(self): # 도시락 가방 목록 확인
        print('# 도시락 가방 목록 확인')
        for mybag in self.dosirak:
            print('이름 : %s, 수량 : %d' % (mybag.name, mybag.gaesu))
            for ban in mybag.banchan:
                print( ban, end='#')
            print()
# end class Bag

#Dosirak 클래스는 Bag 클래스의 포함 대상
class Dosirak:
    def __init__(self, name, gaesu, *banchan):
        self.name = name # 이름
        self.gaesu = gaesu # 개수
        self.banchan = banchan # 반찬
# end class Dosirak

# Bag의 기본 생성자를 이용해서 객체를 생성
mybag = Bag()

do01 = Dosirak('진달래도시락', 7000, '계란 후라이', '김', '마른 멸치')
# Bag의 static 변수인 리스트 dosirak에 Dosirak 생성자로 생성된 객체가 담김
# 사실상 어떤 한 클래스가 다른 클래스 안에 담긴 모양
# 이런 구조를 Has A 관계(구조)라고 함
mybag.put(do01) # 뚜껑이 닫혀서 담지 못함
mybag.open() # 뚜껑 열고
mybag.put(do01) # 도시락 담기
mybag.close() # 가방 닫기
print('-'*20)
do02 = Dosirak('매화도시락', 10000, '고급 어묵', '김치', '단호박 샐러드')
mybag.open()
mybag.put(do02)
mybag.close()