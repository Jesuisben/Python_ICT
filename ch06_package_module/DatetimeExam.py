# DatetimeExam.py
import datetime

now = datetime.datetime.now()
print(type(now))
print('현재 시각 : %s' % str(now))

# strftime : string formatted time의 줄인말입니다.
# 날짜 객체에서 년월일시분초 등의 값을 문자열로 변환해 줍니다.
# 자바의 SimpleDateFormat 클래스도 같이 공부
pattern = '%Y/%m/%d %H:%M:%S'
nowStr = now.strftime(pattern)
print(nowStr)

# timedelta는 시간 사이의 간격을 지정하는 데 사용합니다.
tomorrow = now + datetime.timedelta(days=1)
print('tomorrow :', tomorrow)

# strptime 함수는 문자열 데이터를 datetime 객체로 변환해주는 함수입니다.
pattern = '%Y/%m/%d %H:%M:%S'
someday = datetime.datetime.strptime(nowStr, pattern)
print('someday :', someday)

# datetime 객체 간의 뺄셈 연산은 timedelta 타입이 됩니다.
delta = tomorrow - now
print(type(delta))
print('delta :', delta)

mydate = datetime.date(2024, 3, 6)
print(type(mydate))
print(mydate)

mytime = datetime.time(12, 40, 55)
print(type(mytime))
print(mytime)

# combine 함수는 날짜와 시간을 결합해주는 함수입니다.
newData = datetime.datetime.combine(date=mydate, time=mytime)
print(type(newData))
print(newData)