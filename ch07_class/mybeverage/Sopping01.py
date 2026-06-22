'''
다음 코드를 파이썬으로 작성하되 ch07_class 패키지 아래 mybeverage 패키지 내에 작성해 주세요.

예를 들어서 mybeverage 패키지 내에 Shopping04라는 클래스 이름으로 작성해야 합니다
구현할 클래스는 다음과 같습니다.
Shopping04(메인 클래스)
Beverage04(수퍼 클래스)
Americano04(서브 클래스)
Espresso04(서브 클래스)
Latte04(서브 클래스)


모든 음료(Beverage04)들은 음료 이름(name)과 단가(price)라는 변수를 가지고 있습니다. 그리고, 아메리카노(Americano04)는 투여하는 물량(waterAmount)을,
에스프레소(Espresso04)는 shotCount(샷 추가 회수)를, 라떼(Latte04)는 우유의 타입(milkType)라는 이름으로 개별 변수를 정의하도록 합니다.
서브 클래스마다 다른 이름의 메소드가 존재해야 하는데, 예를 들어 Espresso04는 drinkEspresso(), Latte04는 enjoyLatte(),
아메리카노(Americano04)는 sipAmericano() 등으로 구현해 보세요.


출력 결과 예시
음료 이름 : 아메리카노
단가 : 4000.0
투입된 물의 량 : 250.0ml
아메리카노를(을) 홀짝 홀짝 마십니다.

음료 이름 : 에스프레소
단가 : 5000.0
샷 추가 개수 : 2
맛이 진하고 강렬한 에스프레소를 마십니다.

음료 이름 : 라떼
단가 : 6000.0
우유 타입 : 아몬드 우유
부드럽고 크리미한 라떼를 마십니다.
--------------------------

음료 이름 : 아메리카노
단가 : 4000.0
투입된 물의 량 : 250.0ml
아메리카노를(을) 홀짝 홀짝 마십니다.
--------------------------


음료 이름 : 마이뿌레소
단가 : 2000.0
샷 추가 개수 : 1
맛이 진하고 강렬한 마이뿌레소를 마십니다.
--------------------------

음료 이름 : latte
단가 : 3000.0
우유 타입 : 바나나 우유
부드럽고 크리미한 latte를 마십니다.

음료 아메리카노의 단가는 4000.0이고, 투입할 물의 양은 250.0입니다.
음료 에스프레소의 단가는 5000.0이고, 투입할 샷의 개수는 2개입니다.
음료 라떼의 단가는 6000.0이고, 우유의 타입은 아몬드 우유입니다.

'''
from ch07_class.mybeverage.Beverage import Americano04, Espresso04, Latte04


class Shopping04:
    def __init__(self):
        self.americano = Americano04("아메리카노", 4000.0, 250.0)
        self.espresso = Espresso04("에스프레소", 5000.0, 2)
        self.latte = Latte04("라떼", 6000.0, "아몬드 우유")

    def print_beverages(self):
        print(self.americano)
        print("--------------------------")
        print(self.espresso)
        print("--------------------------")
        print(self.latte)
        print("--------------------------")

        # Additional Beverages
        beverages = [
            Americano04("마이아메리카노", 2000.0, 250.0),
            Espresso04("마이뿌레소", 2000.0, 1),
            Latte04("latte", 3000.0, "바나나 우유")
        ]
        # 리스트에 담긴 음료 객체들을 순차적으로 출력
        for beverage in beverages:
            print(beverage)
            print("--------------------------")

        # 각 음료의 상세정보 출력
        for beverage in beverages:
            if isinstance(beverage, Americano04):
                print(f"음료 {beverage.name}의 단가는 {beverage.price}이고, 투입할 물의 양은 {beverage.waterAmount}입니다.")
            elif isinstance(beverage, Espresso04):
                print(f"음료 {beverage.name}의 단가는 {beverage.price}이고, 투입할 샷의 개수는 {beverage.shotCount}개입니다.")
            elif isinstance(beverage, Latte04):
                print(f"음료 {beverage.name}의 단가는 {beverage.price}이고, 우유의 타입은 {beverage.milkType}입니다.")


# 실행 코드
if __name__ == "__main__":
    shopping = Shopping04()
    shopping.print_beverages()