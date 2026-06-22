# kmdb13.get_movie_people_list.py
import urllib.request
import math
import pandas as pd
import xml.etree.ElementTree as ET

service_key = 'd6ad0a25605d074b615536d66aef6ddd'

def getDataFromWeb(url):
    # 해당 url 정보를 이용하여 웹 사이트에서 json 데이터를 읽어 옵니다.
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200: # HTTP 응답 오케이
            # print('크롤링 성공')
            # read()는 응답 본문을 바이트 스트림으로 변환하고, decode('UTF-8') 메소드는 UTF-8 인코딩을 사용하여 문자열로 변환합니다.
            return response.read().decode('UTF-8')
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
# end def getDataFromWeb

def peopleExtractor(pageNumber, pageSize):
    end_point = 'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml'
    parameter = '?key=' + service_key
    parameter += '&curPage=' + str(pageNumber)
    parameter += '&itemPerPage=' + str(pageSize)

    url = end_point + parameter
    # print(url)

    xmlData = getDataFromWeb(url)

    if xmlData == None:
        return None
    else:
        return xmlData
    # end if
# end def peopleExtractor

# 전체 영화인 목록을 저장할 리스트
totalPeopleList = []

def makePeopleTable(moviePeople):
    for people in moviePeople.find('peopleList'):
        onePeople = tuple() # 1사람 정보를 저장할 튜플
        for unit in people:
            # 1사람 정보를 모두 누적시킵니다.
            onePeople = onePeople + (unit.text, )
        # end inner for

        # 1사람 정보를 list에 추가합니다.
        totalPeopleList.append(onePeople)
        # print('-'*30)
    # end outer for
# end def makePeopleTable

print('크롤링 중입니다. 잠시만 기다려 주세요.')

pageNumber = 1 # 현재 작업 중인 페이지 번호

# 추출할 행 개수로써, 확인해본 결과 최대 100까지 허용함
pageSize = 100

while True:
    peopleData = peopleExtractor(pageNumber, pageSize)
    # print(peopleData)

    # fromstring() : 문자열 → XML 트리로 변환
    xmlPeopleData = ET.fromstring(peopleData)
    # print(type(xmlPeopleData))

    totCnt = int(xmlPeopleData.find('totCnt').text)

    if totCnt == 0:
        print('데이터가 존재하지 않는군요')
        break

    if pageNumber == 1:
        print('1번만 전체 페이지 수를 보여 줍니다.')
        print('전체 개수 : %d' % totCnt)

    totalPage = math.ceil(totCnt / pageSize)
    print('진행중인 페이지 : ' + str(pageNumber) + '/' + str(totalPage))
    makePeopleTable(xmlPeopleData)

    # if pageNumber == totalPage:
    if pageNumber == 100: # 전체 페이지 말고 명시된 페이지까지만 출력하기
        print('마지막 페이지라서 종료합니다.')
        break

    pageNumber += 1
# end while True

print('크롤링이 종료되었습니다.')

# print(totalPeopleList)

filename = 'kmdb_get_movie_people_list.csv'
peopleTable = pd.DataFrame(totalPeopleList)
peopleTable.columns = ['영화인코드', '영화인이름', '영화인이름영문', '분야', '필모리스트']
peopleTable.to_csv(filename, index=False, encoding='UTF-8')
print(filename + ' 파일이 저장되었습니다.')