# JumsuCheck.py
# sample.txt 파일을 읽어서, 총점과 평균을 구하여 result.txt 파일에 기록해 주세요.
'''
readlines() 함수를 이용하여 파일을 읽습니다.
for 반복문을 사용하여 총합을 구합니다.
평균을 구한 다음 write() 함수를 이용하여 파일에 기록합니다.

result.txt 파일의 내용
총점 : 790
평균 : 79.0
'''

print('파일을 읽기 모드로 오픈한다.')
# 읽을 파일
source = open('sample.txt', 'r', encoding='UTF-8')

# 생성할 파일
destination = open('result.txt', 'w', encoding='UTF-8')

# 여기서 처리하세요.
print('\nreadlines() 함수는 모든 라인을 읽어서 리스트로 만들어 준다.')
jumsuList = source.readlines()

total = 0
for jumsu in jumsuList:
    imsi = float(jumsu.strip())
    total += imsi
# end for

average = total / len(jumsuList)

destination.write('총점 : %.2f\n' % total)
destination.write('평균 : %.2f\n' % average)

source.close()
destination.close()

print('작업 종료')