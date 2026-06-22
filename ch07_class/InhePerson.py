class Person:
    def __init__(self, name, age, gender):
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

class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hiredate = hiredate

    def aboutMe(self):
        super().aboutMe()
        print('급여 : ' + str(self.salary))
        print('입사 일자 : ' + self.hiredate)

    def doWork(self):
        print(super().getName() + '열심히 일합시다.', sep='')

# class Employee(Person)

class Student(Person):
    def __init__(self, name, age, gender, subject, grade):
        super().__init__(name, age, gender)
        self.subject = subject
        self.grade = grade

    def aboutMe(self):
        super().aboutMe()
        print('과목 : ' + str(self.subject))
        print('학점 : ' + self.grade)

    def doStudy(self):
        print(super().getName() + '열심히 공부합시다.', sep='')
# class Student(Person)

soo = Employee('김철수', 20, '남자', 50000, '2018/12/25')
soo.aboutMe()
soo.doWork()
print('-'*20)

hee = Student('박영희', 19, '여자', '국어', 'A학점')
hee.aboutMe()
hee.doStudy()
print('-'*20)
print('finished')

# Person 클래스를 상속 받는 Teacher 클래스를 구현해 보세요.
# kim = Teacher('김유신', 40, '남자', '파이썬')
# kim.aboutMe()
# kim.doTeach