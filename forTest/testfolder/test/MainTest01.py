# StringModule 테스트를 위한 메인 모듈

from forTest.testfolder.mystring import StringModule

concat = StringModule.concat("안녕", "하세요")
print(concat)

multiple = StringModule.multiple("안녕")
print(multiple)