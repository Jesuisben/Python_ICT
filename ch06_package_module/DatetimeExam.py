# DatetimeExam.py
import datetime

# datetime.datetime.now() : 현재의 시간을 datetime 객체로 반환함
now = datetime.datetime.now()
print(type(now))
# 출력 : 현재 시각 : 2026-06-25 13:54:46.668484 (668484는 마이크로초)
# datetime 객체인 now를 %s로 포맷팅해서 출력하기 위해 str()로 변환함
print('현재 시각 : %s' % str(now))

# strftime : string formatted time의 줄인말입니다.
# 날짜 객체에서 년월일시분초 등의 값을 문자열로 변환해 줍니다.
# 자바의 SimpleDateFormat 클래스도 같이 공부
pattern = '%Y/%m/%d %H:%M:%S'
# datetime 객체인 now를 내가 원하는 형태로 포맷팅하기 위해서
# strftime(pattern)를 사용함 - str타입으로 반환됨
nowStr = now.strftime(pattern)
print(nowStr)

# timedelta는 시간 사이의 간격을 지정하는 데 사용합니다.
# datetime.timedelta(days=1) : 1일 간격이라는 시간 간격 자체를 나타내는 객체
tomorrow = now + datetime.timedelta(days=1)
print('tomorrow :', tomorrow)

# strptime 함수는 문자열 데이터를 datetime 객체로 변환해주는 함수입니다.
pattern = '%Y/%m/%d %H:%M:%S'
# strptime(문자열, 패턴)
someday = datetime.datetime.strptime(nowStr, pattern)
print('someday :', someday)

# datetime 객체 간의 뺄셈 연산은 timedelta 타입이 됩니다.
# 시간 간격을 알아냄
delta = tomorrow - now
print(type(delta))
print('delta :', delta)

# datetime.date : 날짜(년, 월, 일)만 다루는 클래스
mydate = datetime.date(2024, 3, 6)
print(type(mydate))
print(mydate) # 2024-03-06

# datetime.time : 시간(시, 분, 초)만 다루는 클래스
mytime = datetime.time(12, 40, 55)
print(type(mytime))
print(mytime) # 12:40:55

# combine 함수는 날짜와 시간을 결합해주는 함수입니다.
newData = datetime.datetime.combine(date=mydate, time=mytime)
print(type(newData))
print(newData)