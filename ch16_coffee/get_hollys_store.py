import requests
from bs4 import BeautifulSoup
import pandas as pd

# 크롤링할 기본 URL
hollys_base_url = "https://www.hollysFrame.co.kr/store/korea/korStore2.do"

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='
api_key = 'd2fb0b46a449c5e9e636a0078db80cc7'
header = {'Authorization': 'KakaoAK ' + api_key}

# 주소를 입력 받아서 위도와 경도를 반환해주는 함수 구현하기
def getGeoCoder(address):
    result = ""
    url = url_header + address
    response = requests.get(url, headers=header)
    # print(response) # 성공시 <Response [200]>으로 리턴 됨
    # print(response.json())
    if response.status_code == 200:
        try:
            result_address = response.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(response.status_code) + "]"

    return result
# end def

# 페이지 번호를 추적하여 매장 정보를 가져오는 함수
def get_store_data(page_no):
    parameters = {
        "pageNo": page_no,
        "sido": "서울",  # 서울에 있는 매장만 가져오기
        "gugun": "",
        "store": ""
    }

    # URL에 요청 보내기
    response = requests.get(hollys_base_url, params=parameters)
    if response.status_code != 200:
        print(f"페이지 {page_no} 로드 실패!")
        return []

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    # 테이블에서 매장 정보 추출
    store_table = soup.find('table', {'class': 'tb_store'})
    # all_store = store_table.find_all('tr')[1:]  # 첫 번째 행은 헤더이므로 제외

    if not store_table:
        print(f"페이지 {page_no}에서 테이블을 찾을 수 없습니다.")
        return []

    all_store = store_table.find_all('tr')[1:]  # 헤더 제외한 데이터 행

    if len(all_store) == 0:  # all_store가 비어 있으면 None을 반환
        return None

    stores = [] # 현재 페이지에서 반환될 모든 매장 정보       
    for one_store in all_store:
        td_tags = one_store.find_all('td')
        if len(td_tags) < 6:  # 매장 정보가 부족하면 무시
            continue

        # region = td_tags[0].text.strip()  # 지역
        brand = '할리스' # 브랜드
        name = td_tags[1].text.strip()  # 상호
        # status = td_tags[2].text.strip()  # 현황
        address = td_tags[3].text.strip()  # 주소
        imsi = address.split(' ')
        # sido = imsi[0]
        gu = imsi[1]
        store_services = td_tags[4].text.strip()  # 매장 서비스
        phone_number = td_tags[5].text.strip()  # 전화번호

        geoInfo = getGeoCoder(address)
        # print('geoInfo')
        # print(geoInfo)
        if geoInfo != None:
            latitude = geoInfo[0]  # 위도
            longitude = geoInfo[1]  # 경도
            # print(f'{latitude}, {longitude})')
        else:
            print(address)
            parts = address.split()  # 공백을 기준으로 분리
            address = ' '.join(parts[:-1])  # 마지막 항목 제외하고 다시 합치기

            geoInfo = getGeoCoder(address)
            latitude = geoInfo[0]  # 위도
            longitude = geoInfo[1]  # 경도

        stores.append([brand, name, address, gu, latitude, longitude, store_services, phone_number])
    return stores

# 매장 정보를 저장할 리스트
hollysData = []

# 페이지 번호를 계속 증가시키며 크롤링
page_no = 1
while True:
    print(f"페이지 {page_no} 크롤링 중...")
    stores = get_store_data(page_no)
    if not stores:
        break  # 더 이상 매장 정보가 없으면 종료

    hollysData.extend(stores)
    page_no += 1

# 크롤링한 데이터를 DataFrame으로 변환
hollysFrame = pd.DataFrame(hollysData, columns=["브랜드", "상호", "주소", "군구", '위도', '경도', "매장 서비스", "전화번호"])

# # 위도와 경도에 값이 들어 있지 않은 행 검색하기
# print(hollysFrame[hollysFrame["위도"].isna() | hollysFrame["경도"].isna()])

# 결과 출력
print(f"총 {len(hollysFrame)}개의 매장 정보가 수집되었습니다.")
print(hollysFrame.head())

# CSV 파일로 저장 (선택사항)
hollysFrame.to_csv('hollys_stores.csv', index=False, encoding='utf-8-sig')
