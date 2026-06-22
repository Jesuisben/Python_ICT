import pandas as pd
import urllib.request
import xml.etree.ElementTree as ET

def getDataFromWeb(url):
    # 해당 url 정보를 이용하여 웹 사이트에서 json 데이터를 읽어 옵니다.
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:  # HTTP 응답 오케이
            # print('크롤링 성공')
            return response.read().decode('UTF-8')
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
# end def getDataFromWeb

service_key = 'fd1b397b900f6f6095dda25fe5691f86'

def peopleDetailExtractor(peopleCode):
    # 영화인 코드(peopleCode)를 이용하여 정보를 추출합니다.
    end_point = 'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.xml'
    parameters = '?key=' + service_key
    parameters += '&peopleCd=' + str(peopleCode)
    url = end_point + parameters
    # print(url)

    xmlData = getDataFromWeb(url)

    if xmlData == None:
        return None
    else:
        return xmlData
    # end if
# end def peopleDetailExtractor

totalPeopleList = [] # 영화인 목록을 저장할 리스트

filmoList = [] # 영화인 필모 정보를 저장할 리스트

def makePeopleTable(peopleCodeData):
    # 데이터를 모두 리스트에 저장합니다
    peopleInfo = peopleCodeData.find('peopleInfo')

    if peopleInfo == None:
        return None

    peopleCd = peopleInfo.find('peopleCd').text if peopleInfo.find('peopleCd') is not None else ''
    peopleNm = peopleInfo.find('peopleNm').text if peopleInfo.find('peopleNm') is not None else ''
    peopleNmEn = peopleInfo.find('peopleNmEn').text if peopleInfo.find('peopleNmEn') is not None else ''
    sex = peopleInfo.find('sex').text if peopleInfo.find('sex') is not None else ''
    repRoleNm = peopleInfo.find('repRoleNm').text if peopleInfo.find('repRoleNm') is not None else ''
    homepages = peopleInfo.find('homepages').text if peopleInfo.find('homepages') is not None else ''
    oneTuple = (peopleCd, peopleNm, peopleNmEn, sex, repRoleNm, homepages)

    totalPeopleList.append(oneTuple)

    for filmo in peopleInfo.find('filmos'):
        movieCd = filmo.find('movieCd').text
        movieNm = filmo.find('movieNm').text
        moviePartNm = filmo.find('moviePartNm').text

        someOneFilmo = (peopleCd, movieCd, movieNm, moviePartNm)
        filmoList.append(someOneFilmo)
    # end for
# end def makePeopleTable

peopleFile = 'kmdb_get_movie_people_list.csv'
peopleData = pd.read_csv(peopleFile, encoding='UTF-8')
# print(peopleData.head())

peopleCodeList = [item for item in peopleData['영화인코드']]
# print(peopleCodeList)

print('크롤링 중입니다. 잠시만 기다려 주세요.')

idx = 0
peopleCodeListLength = len(peopleCodeList)

for code in peopleCodeList:
# for code in peopleCodeList[0:3]:
    # 각 사람들의 영화인코드(code)를 이용하여
    xmlData = peopleDetailExtractor(code)
    # print(xmlData)
    # print('영화인 코드 \'' + str(code) + '\'에 대하여 크롤링 중입니다.')

    idx += 1
    print(str(idx) + '/' + str(peopleCodeListLength) + ' 번째 처리중입니다.')

    peopleCodeData = ET.fromstring(xmlData)
    # print(type(peopleCodeData))

    makePeopleTable(peopleCodeData)

    if(idx==100): # 이건 나중에 주석
        break

# end for

print('크롤링이 종료되었습니다.')

# print(totalPeopleList)

# 영화인 상세 정보 기본적인 데이터
filename = 'kmdb_get_movie_people_detail.csv'
peopleTable = pd.DataFrame(totalPeopleList)
# peopleTable.columns = ['영화인코드', '이름', '영문이름', '성별', '역할', '홈페이지']
peopleTable.to_csv(filename, index=False, encoding='UTF-8')
print(filename + ' 파일이 저장되었습니다.')

# 필모와 관련된 정보
filmoFilename = 'kmdb_get_movie_people_filmo.csv'
filmoTable = pd.DataFrame(filmoList)
# filmoTable.columns = ['영화인코드', '영화코드', '영화이름', '역할']
filmoTable.to_csv(filmoFilename, index=False, encoding='UTF-8')
print(filmoFilename + ' 파일이 저장되었습니다.')