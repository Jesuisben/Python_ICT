'''
파이썬을 사용하여 다음 코드를 작성해 주세요.
생성 파일 : Saram02.py, SaramMain02.py

사람의 정보를 나타내는 클래스에서 김유신과 유관순 2명 모두 대한 민국 국적입니다.
이것은 변수를 여러 개 만들 필요 없이 1개만 작성하여 공유를 하게 되면 메모리 효율을 기대할 수 있습니다.
이때 사용하는 키워드가 자바에서는 static이라는 키워드입니다.
변수의 종류는 크게 static(정적), instance(인스턴스), local(지역) 변수 등 3가지 형태의 변수 존재합니다.
각 변수들에 대한 특징을 구분하는 능력을 키우도록 합니다.
'''
from Saram02 import Saram

# 객체 생성 (Instance 변수)
person1 = Saram("김유신", 30)
person2 = Saram("유관순", 18)

# Instance 변수 출력
print(person1.introduce())  # 김유신 소개
print(person2.introduce())  # 유관순 소개

# Static 변수 출력
print(f"{person1.name}의 국적: {person1.nation}")
print(f"{person2.name}의 국적: {person2.nation}")

# Static 변수 변경 (모든 객체에 반영됨)
Saram.change_nation("대한제국")

print(f"{person1.name}의 국적(변경 후): {person1.nation}")
print(f"{person2.name}의 국적(변경 후): {person2.nation}")

# Static 메서드 호출
print(Saram.static_method_demo())
