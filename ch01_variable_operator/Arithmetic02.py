"""
- 요구사항
다음 변수를 사용하여 시간/분/초를 출력하는 프로그램을 만들어 보세요.
TIME = 4000 (초)

- 출력 결과
4000초는 1시간, 6분, 40초입니다
"""

TIME = 4000
imsi = TIME

hour = int(TIME / 3600)
TIME = TIME % 3600

minute = TIME // 60
TIME = TIME % 60

second = TIME

message = '%d초는 %d시간, %d분, %d초입니다.'
print(message % (imsi, hour, minute, second))