print('파일을 읽기 모드로 오픈한다.')
# 읽을 파일
source = open('memdata01.csv', 'rt', encoding='utf-8')
 
# {부서이름:인원수}를 저장할 사전 객체
positionDict = dict()

print('\nreadlines() 함수는 모든 라인을 읽어서 리스트로 만들어 준다.')
linelists = source.readlines()
source.close()

totallist = []
for oneitem in linelists :
    mylist = oneitem.split(',')
    name = mylist[0]
    buseo = mylist[1]
    position = mylist[2]
    jumsu1 = float(mylist[3])*80/1000
    jumsu2 = float(mylist[4])*10/100
    jumsu3 = float(mylist[5])*10/100

    if buseo in positionDict :
        positionDict[buseo] += 1
    else :
        positionDict[buseo] = 1
    # end if  
    total = jumsu1 + jumsu2 + jumsu3
    average = total / 3.0
 
    # %10.2f : 10은 넉넉한 임의의 숫자, .2은 소수점 2자리 까지 표시하려고...
    avg = float('%10.2f' % (average))

    sublist = (name, total, avg)
    totallist.append(sublist)
# end for 

print('\n리스트 정보')
print(totallist )

print('\n사전 정보')
print(positionDict)

print('작업 종료')