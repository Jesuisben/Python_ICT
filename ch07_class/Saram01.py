# Saram01.py
class Saram:
    def __init__(self, name, height, weight, hobby, blood_type):
        """사람 정보를 초기화하는 생성자"""
        self.name = name
        self.height = height
        self.weight = weight
        self.hobby = hobby
        self.blood_type = blood_type

    def display_info(self):
        """사람 정보를 출력하는 메서드"""
        print(f"이름: {self.name}")
        print(f"키: {self.height} cm")
        print(f"몸무게: {self.weight} kg")
        print(f"취미: {self.hobby}")
        print(f"혈액형: {self.blood_type}")
        print("-" * 30)
