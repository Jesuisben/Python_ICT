sourceFile = 'memdata02.csv'
destinationFile = 'result02.txt'

print(sourceFile + '파일을 읽어 가공한 다음 ' + destinationFile + ' 파일에 기록합니다.')

source = open(sourceFile, 'rt', encoding='utf-8')
destination = open(destinationFile, 'wt', encoding='UTF-8')

buDict = {1: '기술지원부', 2: '영업부', 3: '총무부', 4: '인사부'}  # 부서 사전
jikDict = {1: '사원', 2: '주임', 3: '대리', 4: '팀장'}  # 직위 사전

mylist = source.readlines()

separator = '/'  # 문자열 구분자
for oneitem in mylist:
    tempdata = oneitem.split(',')
    name = tempdata[0]
    buseo = buDict[int(tempdata[1])]
    position = jikDict[int(tempdata[2])]
    data = name + separator + buseo + separator + position
    destination.write(data + '\n')
# end for

source.close()
destination.close()

print('작업 종료')