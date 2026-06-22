#  다음 명단(24명)을 이용하여 6명씩 4개조로 만들어 보세요.
names = "김재혁,김창희,김하얀,김홍준,민경환,박진솔,박진주,백상우,변종민,서기은,서준혁,손유정,양경배,엄태현,위진희,유혜진,윤현우,이송민,이승혁,임한울,정소연,정영우,정지웅,최영민"

nameList = names.split(",")
print('원본 데이터 출력')
print(nameList)

import random
random.shuffle(nameList)

print('\n랜덤 섞기 결과')
print(nameList)

MemberSize = 6 # 조원 명수

print('\n팀 배정 결과')
for idx in range(0, len(nameList), MemberSize):
    print('%d조 명단 : %s' % (int(idx/MemberSize)+1, nameList[idx:idx+MemberSize]))