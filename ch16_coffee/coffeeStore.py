#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import folium
import time
import matplotlib.pyplot as plt
import requests

from bs4 import BeautifulSoup

# pip install tqdm : progressBar 구현
from tqdm.notebook import tqdm 
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# In[2]:


chrome_options = webdriver.ChromeOptions() # 크롬 브라우저 옵션
drive_path = 'chromedriver.exe'
myservice = Service(drive_path) # 드라이버 제어를 위한 서비스
driver = webdriver.Chrome(service=myservice, options=chrome_options) # 드라이버 객체
print(type(driver))

wait_time = 10 # 최대 대기 시간 10초
driver.implicitly_wait(wait_time)


# In[3]:


driver.maximize_window() # 윈도우 창 최대화


# In[4]:


starbucks_url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
driver.get(starbucks_url) # 해당 페이지로 이동하기


# In[5]:


# 스타벅스 '서울' 링크 클릭
starbucks_seoul_selector = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, starbucks_seoul_selector))).click()


# In[6]:


# 스타벅스 '서울'-'전체' 링크 클릭
starbucks_seoul_all = '#mCSB_2_container > ul > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, starbucks_seoul_all))).click()


# In[8]:


# 스타벅스 html 코드를 파싱(parsing)해서 html 파일에 기록합니다. 
html = driver.page_source # 해당 페이지의 소스 코드 반환
filename = 'starbucks.html'
htmlFile = open(filename, 'w', encoding='UTF-8')
print(html, file=htmlFile)
htmlFile.close()
print(filename + ' 파일 생성됨')


# In[9]:


# 파싱된 결과를 BeautifulSoup 객체로 생성합니다. 
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))


# In[10]:


container = soup.find('div', id='mCSB_3_container')
storeAll = container.find_all('li')
print('storeAll : %d' % len(storeAll))


# In[11]:


'''
모든 내용들은 white Character 문자열을 제거하도록 합니다.
상호명은 <strong> 태그 내의 문자열을 추출합니다.
주소는 <p> 태그 내의 문자열을 추출하되, '1522-3232'는 공백으로 치환합니다.
구(gu) 정보는 주소에서 추출하도록 합니다.
'''
starbucksData = []

for store in storeAll:
    # print(store)
    brand = '스타벅스'
    name = store.find('strong').text.strip()
    address = store.find('p').text.strip().replace('1522-3232', '')
    imsi = address.split(' ')
    # sido = imsi[0]
    gu = imsi[1]
    latitude = store['data-lat'] # 위도
    longitude = store['data-long'] # 경도
    
    starbucksData.append([brand, name, address, gu, latitude, longitude])
    # break
# end for

print(len(starbucksData))


# In[12]:


'''
<li class="quickResultLstCon" data-code="3762" data-hlytag="null" data-index="0" 
        data-lat="37.501087" data-long="127.043069" data-name="역삼아레나빌딩" 
        data-storecd="1509" style="background:#fff"> 
    <strong data-my_siren_order_store_yn="N" 
        data-name="역삼아레나빌딩" data-store="1509" data-yn="N">역삼아레나빌딩  
    </strong> 
    <p class="result_details">서울특별시 강남구 언주로 425 (역삼동)
        <br/>1522-3232
    </p> 
    <i class="pin_general">리저브 매장 2번</i>
</li>
'''


# In[13]:


sbDataFrame = pd.DataFrame(starbucksData)
sbDataFrame.columns = ['브랜드', '상호', '주소', '군구', '위도', '경도']
sbDataFrame.head()


# In[14]:


print('위도 누락 데이터 개수 : %d' % sbDataFrame['위도'].isnull().sum())
print('경도 누락 데이터 개수 : %d' % sbDataFrame['경도'].isnull().sum())


# In[15]:


guList = list(sbDataFrame['군구'].unique())
print('서울시 구 목록 개수 : %d' % len(guList))
print(guList)


# In[16]:


eyida_url = 'https://www.ediya.com/contents/find_store.html'
driver.get(eyida_url) #  


# In[17]:


# 이디야 '매장명'과 '주소' 검색에서 '주소' 클릭
ediya_address_selector = '#contentWrap > div.contents > div > div.store_search_pop > ul > li:nth-child(2) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ediya_address_selector))).click()


# In[18]:


# 누락된 위도와 경도 정보는 kakao api를 이용하여 채워 넣도록 합니다.
# https://developers.kakao.com/
# kakao에 로그인하여 API 키 발급 받기


# In[19]:


url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='
api_key = '16f486bc90ddf8c917b0e903b6bb3ceb'
header = {'Authorization': 'KakaoAK ' + api_key}


# In[20]:


def getGeoCoder(address):
    result = ""
    url = url_header + address
    r = requests.get(url, headers=header)
    #print(r) # 성공시 <Response [200]>으로 리턴 됨
    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result
# end def


# In[21]:


'''
위 경도 변환이 안되는 주소들
서울 노원구 한글비석로 409 (상계동) 1~2층
서울 동작구 사당로16가길 96 (사당동) 1,2층
서울 마포구 백범로 100 (대흥동)
서울 영등포구 영등포로35길 19 (영등포동6가)
'''

# 한 개의 매장 테스트
geoInfo = getGeoCoder('서울 중랑구 망우로 460 (망우동)') # 잘 동작하는 주소
# geoInfo = getGeoCoder('서울 노원구 한글비석로 409 (상계동) 1~2층') # NoneType이 리턴되는 주소
geoInfo


# In[22]:


text = r"dddpanLatTo('0','0','0');fnMove();"
text.index("panLatTo('0','0'")


# In[23]:


'''
매장 1개 정보 
<dt> 태그가 상호, <dd> 태그가 주소
<li class="item">
    <a href="#c" onclick="panLatTo('0','0','0');fnMove();">
    <div class="store_thum">
        <img src="../images/customer/store_thum.gif"/>
    </div>
    <dl>
        <dt>강남YMCA점</dt>
        <dd>서울 강남구 논현동</dd>
    </dl>
    </a>
</li>

위도/경도 추출 결과 : 'a' 태그의 'onclick'에 다음과 같은 값들이 들어 있습니다.
케이스 01
panLatTo('0','0','14');fnMove();

케이스 02
panLatTo('126.929036226245','37.489287127719','7');fnMove();

케이스 03
panAddTo('서울 관악구 보라매로 62 (봉천동, 보라매삼성아파트)','8');fnMove();
'''


# In[26]:


eyidaData = []

for gu in tqdm(guList):    
    ediya_search_keyword_css = '#keyword'
    
    # 이디야 주소 검색어 초기화
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ediya_search_keyword_css))).clear()
    
    # 이디야 주소 검색어 입력
    # f"서울 {gu}" : f-string 기법, 서울 중구, 서울 마포구 등등
    WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, ediya_search_keyword_css))).send_keys(f"서울 {gu}")

    # 이디야 주소 검색 버튼 클릭
    ediya_search_button_css = '#keyword_div > form > button'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ediya_search_button_css))).click()

    # 이디야 매장 정보 수집
    html = driver.page_source

    # 개별 구에 대한 결과를 파일로 저장해 봅니다.
    filename = open(f"서울 {gu}.html", 'w', encoding='UTF-8')
    print(html, file=filename)
    filename.close()
    # print(f"서울 {gu}.html 파일 생성")

    soup = BeautifulSoup(html, 'html.parser')
    ul_tag = soup.find('ul', id='placesList')
    
    ediyaAll = ul_tag.find_all('li')
    for store in ediyaAll: 
        # print(store)
        brand = '이디야'
        name = store.find('dt').text.strip()
        address = store.find('dd').text.strip()
        imsi = address.split(' ')
        sido = imsi[0] 
        gu = imsi[1]

        # 위도/경도 정보가 들어 있는 문자열 
        text = store.find('a')['onclick'] 
        temp = text # 중간에 변형이 될 수 있으므로 임시 복사

        latitude = np.nan
        longitude = np.nan
        latLong = ['0', '0']  # Initialize latLong to a default value
        
        if text.startswith("panLatTo"): 
            # 올바른 위도/경도가 아님
            try:
                if text.index(r"panLatTo('0','0'") == 0: 
                    geoInfo = getGeoCoder(address) 
                    if geoInfo != None:
                        latitude = geoInfo[0] # 위도
                        longitude = geoInfo[1] # 경도
                    else:
                        print(address)                
            except ValueError as err:
                # 올바른 위도/경도입니다.
                latLong = text.replace(r"panLatTo('", '').replace(r"');fnMove();", '')
                latLong = latLong.split("','")
        
                latitude = latLong[1] 
                longitude = latLong[0]                
            # end try

        else: # 'panAddTo'으로 시작하는 경우
            geoInfo = getGeoCoder(address) 
            if geoInfo != None:
                latitude = geoInfo[0] # 위도
                longitude = geoInfo[1] # 경도
            else:
                print(address)
        # end if

        # 올바른 위도 경도 형식이 아니면
        if latLong[1] == '0' or latLong[0] == '0':            
            # 카카오 지도 api 이용하여 위도와 경도를 취득합니다.
            geoInfo = getGeoCoder(address) 
            if geoInfo != None:
                latitude = geoInfo[0] # 위도
                longitude = geoInfo[1] # 경도
            else:
                print(address)
        # end if
        
        eyidaData.append([brand, name, address, gu, latitude, longitude, temp])
        # break
    # end inner for
    # break
# end outer for 

print('이디야 매장 개수 : %d' % len(eyidaData))


# In[27]:


eyidaDataFrame = pd.DataFrame(eyidaData)
eyidaDataFrame.columns = ['브랜드', '상호', '주소', '군구', '위도', '경도', 'temp']
eyidaDataFrame.head()


# In[28]:


print('위도 누락 데이터 개수 : %d' % eyidaDataFrame['위도'].isnull().sum())
print('경도 누락 데이터 개수 : %d' % eyidaDataFrame['경도'].isnull().sum())


# In[29]:


print('스타벅스 매장 개수 : %d' % len(sbDataFrame))
print('이디야 매장 개수 : %d' % len(eyidaDataFrame))


# In[30]:


# 임시 컬럼 제거
eyidaDataFrame = eyidaDataFrame.drop('temp', axis=1)
coffeeFrame = pd.concat([sbDataFrame, eyidaDataFrame])
print('전체 매장 개수 : %d' % len(coffeeFrame))


# In[31]:


filename = 'coffeeList.csv'
coffeeFrame.to_csv(filename, encoding='CP949', index=False)
# coffeeFrame.to_csv(filename, encoding='UTF-8', index=False)
print(filename + ' 파일 저장됨')


# In[32]:


mapFrame = coffeeFrame[coffeeFrame['위도'].notnull()]
print('위도/경도 누락된 행 제거 후 매장 개수 : %d' % len(mapFrame))


# In[36]:


# Map 선언
seoul_center = [37.535855, 126.991558]
coffeeMap = folium.Map(location=seoul_center, zoom_start=11.5, control_scale=True, tiles='openstreetmap')

for idx, rows in mapFrame.iterrows():
    # 브랜드별 마커 색상 설정
    if rows['브랜드'] == '이디야':
        mk_color = 'darkblue'
        ic_color = 'white'
    elif rows['브랜드'] == '스타벅스':
        mk_color = 'green'
        ic_color = 'white'
# end for

# 지도 마커 생성
folium.Marker(
    location=[rows['위도'], rows['경도']],
    popup = rows['주소'],
    tooltip = rows['브랜드'],
    icon = folium.Icon(
        color = mk_color,
        icon_color = ic_color,
        icon = 'coffee',
        prefix = 'fa',
    )
).add_to(coffeeMap)
    
coffeeMap


# In[ ]:





# In[34]:


coffeeMap

