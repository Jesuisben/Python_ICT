'''
사람의 정보를 나타내기 위하여 필요한 정보를 나열해 보도록 합시다.
이름/키/몸무게/취미/혈액형 등이 존재합니다.
이러한 정보들을 클래스를 이용하여 출력하는 프로그램을 작성해 보세요.

'''
# SaramMain01.py
from Saram01 import Saram

# 사람 객체 생성
person1 = Saram("김철수", 175, 70, "독서", "A형")
person2 = Saram("이영희", 160, 55, "영화 감상", "O형")
person3 = Saram("박민준", 180, 80, "운동", "B형")

# 사람 정보 출력
print("=== 사람 정보 출력 ===")
person1.display_info()
person2.display_info()
person3.display_info()
