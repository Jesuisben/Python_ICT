class Saram:
    # Static 변수 (모든 인스턴스가 공유하는 변수)
    nation = "대한민국"

    def __init__(self, name, age):
        # Instance 변수 (각 객체마다 별도로 저장됨)
        self.name = name
        self.age = age

    def introduce(self):
        # Local 변수 (메서드 내에서만 사용되는 변수)
        greeting = f"안녕하세요, 저는 {self.name}이고, {self.age}살입니다."
        return greeting

    @classmethod
    def change_nation(cls, new_nation):
        """ Static 변수(nation) 변경을 위한 클래스 메서드 """
        cls.nation = new_nation

    @staticmethod
    def static_method_demo():
        """ Static 메서드 예제 (객체 상태와 무관한 독립적인 기능 수행) """
        return "이것은 static method입니다."
