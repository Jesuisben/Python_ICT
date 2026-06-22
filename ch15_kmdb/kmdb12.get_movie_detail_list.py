import urllib.request
import json, math
import pandas as pd
from json import JSONDecodeError

service_key = 'fd1b397b900f6f6095dda25fe5691f86'

def getDataFromWeb(url):
    # 해당 url 정보를 이용하여 웹 사이트에서 json 데이터를 읽어 옵니다.
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200: # HTTP 응답 오케이
            # print('크롤링 성공')
            return response.read().decode('UTF-8')
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
# end def getDataFromWeb

def movieExtractor(movieCode):
    # 영화 코드 movieCode를 이용하여 json 데이터를 추출합니다.
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    parameters = '?key=' + service_key
    parameters += '&movieCd=' + movieCode
    url = end_point + parameters
    # print(url)

    jsonData = getDataFromWeb(url)

    if jsonData == None:
        return None
    else:
        try:
            return json.loads(jsonData)
        except JSONDecodeError as err:
            print('JSON 데이터에 문제가 있습니다.')
            print(err)
            return None
        # end try
    # end if
# end def movieExtractor(movieCide)

# # movieCd는 차후 파일에서 읽어 들일 예정
# movieCd = '20124079'

# '영화 목록' 서비스에서 크롤링한 엑셀 파일
kmdbData = pd.read_csv('kmdb_get_movie_list_old.csv', encoding='UTF-8')
print(kmdbData.columns)
print(len(kmdbData))
print(kmdbData.head()) # opp) tail()

# 모든 영화들의 영화 코드(movieCd)를 리스트로 만듭니다.
movieCodeList = list(item for item in kmdbData['movieCd'])
# print(movieCodeList)



cnt = 0 # 카운터 변수
movieCodeLength = len(movieCodeList) # 영화 전체 개수
totalDetailList = list() # 전체 목록을 저장할 리스트

# 영문 필드에 대응하는 한글 이름을 사전으로 작성합니다.
hangulName = {'movieNm':'영화명', 'showTm':'상영시간', 'prdtYear':'제작연도', 'openDt':'개봉연도', 'typeNm':'영화유형'}

# 기존 사전에 요소 추가함
hangulName['nationNm'] = '국가명'
hangulName['genreNm'] = '장르명'

# 주의) "배우이름"과 "감독이름"은 둘 다 'peopleNm'으로 동일한 이름을 사용하고 있습니다.
# 차후 if 구문으로 처리할 예정입니다.
hangulName['peopleNm'] = '배우이름'


# 멀티 정보를 담고 있는 요소들의 하위 카테고리 이름 정보를 담는 사전
subtractDict = {'nations':'nationNm', 'genres':'genreNm', 'directors':'peopleNm', 'actors':'peopleNm'}


print('크롤링 중입니다. 잠시만 기다려 주세요.')

# 전체 영화 코드들을 반복하여 세부 정보들을 추출합니다.
for movieCode in movieCodeList:
# for movieCode in movieCodeList[0:3]: # 편의상 영화 3개만 추출합니다.
    cnt += 1
    print(str(cnt) + '/' + str(movieCodeLength) + '번째 작업중입니다.')

    movieData = movieExtractor(movieCode)
    # print('movieData 결과')
    # print(movieData)

    try:
        onemovie = movieData['movieInfoResult']['movieInfo']
    except KeyError as err:
        print(err)
        # 오류 발생시 이번 거 무시하고 next step을 진행하시오.
        continue
    # end try

    # 목록에 저장하고자 하는 컬럼 리스트
    concern = ['movieNm', 'showTm', 'prdtYear', 'openDt', 'typeNm']
    for element in concern:
        sublist = list()
        sublist.append(movieCode) # 영화 코드
        sublist.append(hangulName[element])
        sublist.append(onemovie[element])
        totalDetailList.append(sublist)
    # end inner for

    # 하위 요소가 중첩된 내용들은 for 구문을 이용하여 반복 처리하도록 합니다.
    # 항목이 5개 이상인 항목들은 5개(변수 maxLimit 참조)까지만 추출하도록 하겠습니다.
    maxLimit = 5

    multiple = ['nations', 'genres', 'directors', 'actors']
    for element in multiple:
        # print('멀티 컬럼 이름 : ' + element)
        # print('서브 항목 이름 : ' + subtractDict[element])
        nodeList = onemovie[element]
        # print(len(nodeList))

        idx = 0 # 카운터 변수
        # 슬라이싱으로 최대 항목 maxLimit까지만 추출함
        for node in nodeList[0:maxLimit]:
            sublist = list()
            sublist.append(movieCode)  # 영화 코드

            # 배우와 감독 이름의 하위 카테고리 이름이 동일하기 때문에 여기서 분기 처리해 줍니다.
            if element == 'directors':
                hangul_name = '감독이름'
            else:
                hangul_name = hangulName[subtractDict[element]]
            # end if

            idx += 1
            # 여러 사람이 존재하므로 일련 번호 붙이기
            hangul_name = hangul_name + str(idx).zfill(2)
            # print(hangul_name)

            sublist.append(hangul_name)  # 하위 요소의 이름
            sublist.append(node[subtractDict[element]]) # 하위 요소가 가지고 있는 값
            totalDetailList.append(sublist)
        # end for
    # end inner for
# end outer for

print('크롤링이 끝났습니다.')

# 영화 상세 정보를 담을 데이터 프레임
movieTable = pd.DataFrame(totalDetailList)
mycolumns = ['movieCode', 'key', 'value']
movieTable.columns = mycolumns

filename = 'kmdb_get_movie_detail_list.csv'

movieTable.to_csv(filename, index=False, encoding='UTF-8')
print(f'{filename} 파일이 저장되었습니다.')