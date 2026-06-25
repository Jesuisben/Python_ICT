# 상속 (수퍼 클래스 / 서브 클래스)
class Person:
    def __init__(self, name, age, gender):
        # 일반화 : 서브 클래스들의 공통분모 설정
        # 서브 클래스에서 오버라이딩 할 예정
        self.name = name
        self.age = age
        self.gender = gender

    def getName(self):
        return self.name + '님 '

    def aboutMe(self):
        print('이름 : ' + self.name)
        print('나이 : ' + str(self.age))
        print('성별 : ' + self.gender)
# class Person

# 상속 : class 서브클래스(수퍼클래스)
class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        # 오버라이딩
        super().__init__(name, age, gender)
        self.salary = salary
        self.hiredate = hiredate

    def aboutMe(self):
        # 오버라이딩
        super().aboutMe()
        print('급여 : ' + str(self.salary))
        print('입사 일자 : ' + self.hiredate)

    def doWork(self):
        # sep= : 구분자 지정
        print(super().getName() + '열심히 일합시다.', sep='')

# class Employee(Person)

class Student(Person):
    def __init__(self, name, age, gender, subject, grade):
        # 오버라이딩
        super().__init__(name, age, gender)
        self.subject = subject
        self.grade = grade

    def aboutMe(self):
        # 오버라이딩
        super().aboutMe()
        print('과목 : ' + str(self.subject))
        print('학점 : ' + self.grade)

    def doStudy(self):
        print(super().getName() + '열심히 공부합시다.', sep='')
# class Student(Person)

class Teacher(Person):
    def __init__(self, name, age, gender, skill):
        super().__init__(name, age, gender)
        self.skill = skill

    def aboutMe(self):
        super().aboutMe()
        print("강의 : " + self.skill)

    def doTeach(self):
        print(super().getName() + "열심히 가르칩시다.", sep="")
# class Teacher(Person)

# 객체 : soo
# 생성자 : Employee('김철수', 20, '남자', 50000, '2018/12/25')
soo = Employee('김철수', 20, '남자', 50000, '2018/12/25')
soo.aboutMe()
soo.doWork()
print('-'*20)

hee = Student('박영희', 19, '여자', '국어', 'A학점')
hee.aboutMe()
hee.doStudy()
print('-'*20)

# Person 클래스를 상속 받는 Teacher 클래스를 구현해 보세요.
kim = Teacher('김유신', 40, '남자', '파이썬')
kim.aboutMe()
kim.doTeach()
print('finished')