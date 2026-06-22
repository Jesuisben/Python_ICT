# Saram03.py

class Person:
    def __init__(self, name, height, weight, hobby, blood_type):
        self.name = name  # 이름
        self.height = height  # 키
        self.hobby = hobby  # 취미
        self.blood_type = blood_type  # 혈액형
        self.__weight = weight  # 몸무게 (숨김 처리)

    # Getter: 몸무게를 반환
    def get_weight(self):
        return self.__weight

    # Setter: 몸무게를 설정
    def set_weight(self, weight):
        if weight > 0:  # 몸무게가 0보다 클 때만 설정
            self.__weight = weight
        else:
            print("몸무게는 0보다 커야 합니다.")

    def display_info(self):
        print(f"이름: {self.name}")
        print(f"키: {self.height}")
        print(f"취미: {self.hobby}")
        print(f"혈액형: {self.blood_type}")
        print(f"몸무게: {self.get_weight()}")  # getter를 사용하여 몸무게 출력
