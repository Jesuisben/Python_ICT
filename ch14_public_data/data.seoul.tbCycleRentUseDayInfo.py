import requests
from itertools import count

''' 
서울시 공공 자전거 이용 정보(일별)
'''
accessToken = '6a776b74577567633130347170457359' # 인증키
pageSize = 1000 # 한번에 읽어 들일 데이터 건수
totalBicycle = list()# 모든 데이터가 저장될 리스트

startYear, endYear = 2024, 2025
startMonth, endMonth = 3, 4
startDay, endDay = 1, 13

print('크롤링을 시작합니다. 잠시만 기다려 주세요.')

for year in range(startYear, endYear):
    for month in range(startMonth, endMonth):
        for day in range(startDay, endDay):
            search_date = str(year) + str(month).zfill(2) + str(day).zfill(2)
            print('\n대여 년월일자 : ' + search_date)

            # count() 함수는 반복 회수가 얼마인지 모를 때....
            # while(True)와 거의 유사한 개념
            for pageNumber in count(): #range(2):
                beginRow = str(pageNumber * pageSize + 1)
                endRow = str((pageNumber + 1) * pageSize)

                url = 'http://openapi.seoul.go.kr:8088/'
                url += accessToken
                url += '/json/tbCycleRentUseDayInfo/'
                url += beginRow + '/'
                url += endRow + '/'
                url += search_date
                # print(url)

                message = '일자 : ' + search_date + ', 범위 : ' + beginRow + '~' + endRow
                print(message)

                response = requests.get(url)
                jsonData = response.json()
                # print(jsonData)

                try:
                    dataList = jsonData['cycleRentUseDayInfo']['row']

                    for data in dataList :
                        totalBicycle.append(data)
                except Exception as err:
                    print('더 이상 데이터가 존재하지 않아서 오류가 발생하였습니다.')
                    # print(err)
                    break # 오류가 발생했으므로, 강제로 멈춰 줍니다.

        # end for day
    # end for month
# end for year

print('크롤링이 종료 되었습니다.')

start_date = str(startYear) + str(startMonth).zfill(2) + str(startDay).zfill(2)
end_date = str(endYear-1) + str(endMonth-1).zfill(2) + str(endDay-1).zfill(2)

filename = './../data/cycleRentUseDayInfo' + '(' + start_date + '~' + end_date + ')' + '.csv'

import pandas as pd
myframe = pd.DataFrame(totalBicycle)
myframe.to_csv(filename)
print(filename + ' 파일이 저장되었습니다.')