import urllib.request
import urllib.parse
import json, math
import pandas as pd

# 해당 사이트에서 발급 받은 키
service_key = 'd6ad0a25605d074b615536d66aef6ddd'


# 웹 페이지에서 데이터를 가져 오는 함수
def getDataFromWeb(url):
    request = urllib.request.Request(url) #  요청 객체
    
    try:
        response = urllib.request.urlopen(request) # 응답 객체
        if response.getcode() == 200: # HTTP 응답 코드 200(OK) 확인
            return response.read().decode('UTF-8') # 바이트로 변환 후 다시 문자열로 반환
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
    # end try
# end def getDataFromWeb(url)


# 영화 정보를 추출해주는 함수
def movieExtractor(pageNumber, pageSize, thisYear):
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'

    # API 요청 파라미터 구성
    parameter = f'?key={service_key}&curPage={pageNumber}&itemPerPage={pageSize}&openStartDt={thisYear}'

    # # 검색할 영화명 인코딩
    # movie_name = '행복의 나라'
    # encoded_movie_name = urllib.parse.quote(movie_name, encoding='UTF-8')
    # parameter += f'&movieNm={encoded_movie_name}'
    # print(f'[{encoded_movie_name}]')

    url = end_point + parameter

    jsonData = getDataFromWeb(url)
    if jsonData is None:
        return None

    try:
        return json.loads(jsonData)
    except Exception as err:
        print('JSON 데이터에 문제가 있습니다.', err)
        return None
    # end try        
# def movieExtractor


# 영화 정보를 저장할 데이터 프레임
movieTable = pd.DataFrame()


# JSON 데이터를 판다스 데이터 프레임으로 반환해주는 함수
def makeMovieTable(movieData):
    global movieTable  # 전역 변수 사용 선언

    for onemovie in movieData['movieListResult']['movieList']:
        onedict = {
            'movieCd': onemovie['movieCd'],
            'movieNm': onemovie['movieNm'],
            'movieNmEn': onemovie['movieNmEn'],
            'prdtYear': onemovie['prdtYear'],
            'openDt': onemovie['openDt'],
            'typeNm': onemovie['typeNm'],
            'prdtStatNm': onemovie['prdtStatNm'],
            'nationAlt': onemovie['nationAlt'],
            'genreAlt': onemovie['genreAlt'],
            'repNationNm': onemovie['repNationNm'],
            'repGenreNm': onemovie['repGenreNm']
        }

        # 기존 데이터 프레임에 현재 프레임을 누적
        oneframe = pd.DataFrame(onedict, index=[0])
        
        # 전역 변수 movieTable을 함수 내부에서 다시 할당(=)했기 때문에, Python은 이를 지역 변수로 인식합니다.
        # 따라서, global 키워드를 사용하여 전역 변수라고 선언해 주어야 합니다.
        movieTable = pd.concat([movieTable, oneframe])  # 기존 데이터프레임과 병합

    print('-' * 30)


print('크롤링 중입니다. 잠시만 기다려 주세요.')

# 설정 값
startYear, endYear = 2024, 2025
pageSize = 100  # 최대 100개까지 가능

# 연도별 데이터 크롤링
for thisYear in range(startYear, endYear):
    print(f'{thisYear}년도 크롤링 중입니다.')
    pageNumber = 1

    while True:
        movieData = movieExtractor(pageNumber, pageSize, thisYear)
        print(movieData)
        print('-'*100)
        
        if movieData is None:
            break

        try:
            totCnt = movieData['movieListResult']['totCnt']
        except Exception:
            pageNumber += 1
            continue
        # end try            

        if pageNumber == 1:  # 첫 페이지에서 전체 개수 출력
            print(f'데이터 총 개수 : {totCnt}')

        if totCnt == 0:  # 데이터가 없으면 종료
            break

        totalPage = math.ceil(totCnt / pageSize)
        print(f'진행 중인 페이지 : {pageNumber}/{totalPage}')

        makeMovieTable(movieData)

        if pageNumber == totalPage:
            break  # 마지막 페이지 도달 시 종료

        pageNumber += 1  # 다음 페이지로 이동
    # end while
# end for

print('크롤링이 끝났습니다.')

# 데이터 확인
print(movieTable)
print(type(movieTable))
print(movieTable.info())

# CSV 파일 저장
filename = 'kmdb_get_movie_list.csv'
movieTable.to_csv(filename, index=False, encoding='UTF-8')
print(f'{filename} 파일이 저장되었습니다.')
