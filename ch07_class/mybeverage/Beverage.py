class Beverage04:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"음료 이름 : {self.name}\n단가 : {self.price}"


class Americano04(Beverage04):
    def __init__(self, name, price, waterAmount):
        super().__init__(name, price)
        self.waterAmount = waterAmount

    def sipAmericano(self):
        return f"{self.name}를(을) 홀짝 홀짝 마십니다."

    def __str__(self):
        return f"{super().__str__()}\n투입된 물의 량 : {self.waterAmount}ml\n{self.sipAmericano()}"

class Espresso04(Beverage04):
    def __init__(self, name, price, shotCount):
        super().__init__(name, price)
        self.shotCount = shotCount

    def drinkEspresso(self):
        return f"맛이 진하고 강렬한 {self.name}를 마십니다."

    def __str__(self):
        return f"{super().__str__()}\n샷 추가 개수 : {self.shotCount}\n{self.drinkEspresso()}"


class Latte04(Beverage04):
    def __init__(self, name, price, milkType):
        super().__init__(name, price)
        self.milkType = milkType

    def enjoyLatte(self):
        return f"부드럽고 크리미한 {self.name}를 마십니다."

    def __str__(self):
        return f"{super().__str__()}\n우유 타입 : {self.milkType}\n{self.enjoyLatte()}"


