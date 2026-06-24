# test.py
# exam.py의 __name__ 변수의 값이 ch06_package_module.exam 이걸로 바뀜
# exam.py를 불러오는 순간 exam.py 파일 전체가 실행됨(함수 생성 등)
from ch06_package_module.exam import mysum

su01, su02 = 3, 5

result = mysum(su01, su02)
print(result)

# 여기서의 __name__ 변수는 test.py의 변수라서 값이 __main__으로 나옴
print("모듈 %s가 종료되었습니다." % __name__)