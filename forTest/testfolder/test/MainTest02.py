# TypeModule 테스트를 위한 메인 모듈

from forTest.testfolder.typechange import TypeModule

mklist = TypeModule.mklist("안녕", "하세요")
print(mklist)

mkMultiList = TypeModule.mkMultiList("안녕", "하세요")
print(mkMultiList)