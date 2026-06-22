import requests
'''
공공자전거 대여소 정보(23.12월 기준).csv
'''
accessToken = '이것을깃허브에올리면안될듯한데'

# 호출시 시스템 부하로 한번에 최대 1,000건를 초과할수 없습니다.
pageSize = 1000 # 1회당 최대 호출 건수

totalBicycle = list()

print('데이터 수집 시작')

# Python에서 무한 반복을 수행할 때 itertools.count() 함수를 사용할 수 있습니다.
import itertools

for pageNumber in itertools.count():
    beginRow = str(pageNumber * pageSize + 1)
    endRow = str((pageNumber+1) * pageSize)

    url = 'http://openapi.seoul.go.kr:8088/'
    url += accessToken
    url += '/json/bikeList/'
    url += beginRow + '/'
    url += endRow + '/'
    print(url)

    response = requests.get(url)
    # print(dir(response))
    jsonData = response.json()
    # print(jsonData)

    try:
        datalist = jsonData['rentBikeStatus']['row']
        # print(len(datalist))

        for data in datalist:
            totalBicycle.append(data)

    except Exception as err:
        print('더 이상 데이터가 없어서 오류가 발생하였습니다.')
        print(f'오류 내용 : {err}')
        break
    # end try
# end for

print('데이터 수집 끝')

filename = './../data/bikeList.csv'

import pandas as pd

myframe = pd.DataFrame(totalBicycle)
myframe.to_csv(filename)
print(filename + ' 파일이 저장되었습니다.')