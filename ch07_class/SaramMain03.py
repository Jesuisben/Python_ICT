'''
파이썬을 사용하여 다음 코드를 작성해 주세요.
생성 파일 : Saram03.py, SaramMain03.py

사람의 정보를 나타내기 위한 변수는 이름/키/몸무게/취미/혈액형 등이 존재합니다.
몸무게는 개인적으로 숨기고 싶은 데이터입니다.
이 데이터는 클래스 외부에서 참조하지 못하게 접근 지정자를 이용하여 숨기고 싶습니다.
또한, 숨겨진 데이터를 간접적으로 우회하여 조회하기 위한 방법인 getter, setter에 대하여 숙지하도록 합니다.
또한, 인스턴스 자신을 의미하는 this 키워드에 대하여 살펴 보도록 합니다.

'''



# SaramMain03.py

from Saram03 import Person

# 사람 인스턴스 생성
person1 = Person(name="홍길동", height=175, weight=70, hobby="독서", blood_type="O")

# 사람 정보 출력
person1.display_info()

# 몸무게 수정
person1.set_weight(75)

# 수정된 몸무게 출력
print("수정된 몸무게:")
person1.display_info()

# 잘못된 몸무게 값 설정 시도
person1.set_weight(-5)
