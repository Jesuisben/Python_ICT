import re

# 긍정형 전방 탐색 기법을 이용하여 .com / .net이 아닌 이메일 주소는 제외하도록 합니다.
maillist = ['park@gmail.com', 'kim@daum.net', 'lee@myhome.co.kr']

regex = '.*[@].*[.](?:com$|net$).*$'

pattern = re.compile(regex)

for item in maillist :
    if pattern.match(item) :
        print('주소', item, ': True')
    else :
        print('주소', item, ': False')

# 주소 park@gmail.com : True
# 주소 kim@daum.net : True
# 주소 lee@myhome.co.kr : False