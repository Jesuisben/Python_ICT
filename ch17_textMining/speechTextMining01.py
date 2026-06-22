'''
관련 파일
    윤석열 제20대 대통령 취임사.txt
    user_dic.txt
    stopword.txt
    alice_color.png

설치할 라이브러리
    pip install konlpy <- 한글 형태소 분석 라이브러리
    pip install nltk <- 자연어 처리 툴킷
    pip install wordcloud <- 워드 클라우드
'''
import os
javahome = 'JAVA_HOME'
# os.environ[javahome] = r'C:\Program Files\Java\jdk-12.0.1\bin\server'
os.environ[javahome] = r'C:\Program Files\Java\jdk-12.0.2\bin\server'

print(javahome in os.environ)

dataInFolder = './../data/'
filename = dataInFolder + '윤석열 제20대 대통령 취임사.txt'

speech = open(filename, mode='r', encoding='UTF-8').read()
# print(speech)

# 사용자 정의 단어들을 저장해 놓은 사전 파일을 읽습니다.
# 사용자가 최소 형태소를 커스트 마이징 하려면, 이 파일에 기록해 두세요.
user_dict = dataInFolder + 'user_dic.txt' # 사용자 단어 정의 사전

from konlpy.tag import Komoran

komo = Komoran(userdic=user_dict) # 형태소 분석 객체 생성

# nouns() 함수는 명사를 추출해 줍니다.
token_list = komo.nouns(speech)

# print('토큰 목록')
# print(token_list)

# 불용어(stopword)는 빈도 수는 많지만, 분석시 크게 의미를 부여하지 않아도 되는 단어들을 의미합니다.
stopword_file = dataInFolder + 'stopword.txt' # 불용어 파일
stop_file = open(stopword_file, mode='r', encoding='UTF-8').readlines()
stop_words = [word.strip() for word in stop_file]

# print('불용어 목록')
# print(stop_words)

new_token_list = [word for word in token_list if word not in stop_words]
print('불용어를 제외한 토큰 목록')
# print(new_token_list)

# 집합을 이용하여 불용어 처리가 잘 되었는 지 확인합니다.
set_old_token = set(token_list)
set_new_token = set(new_token_list)
difference = set_old_token.difference(set_new_token)

# print('불용어로 처리된 단어 목록 확인')
# print(difference)

# nltk : National Language ToolKit
import nltk

# 단어의 빈도 수를 내림차순 정렬하여 상위 bindo_size개만 추출합니다.
nltk_token = nltk.Text(tokens=new_token_list)
bindo_size = 500 # 빈도 수
token_data = nltk_token.vocab().most_common(bindo_size)

# print('토큰과 빈도 수 확인')
# print(token_data)

# 해당 목록을 csv 파일로 저장합니다.
import pandas as pd
filename = dataInFolder + 'word_list.csv'
dataFrame = pd.DataFrame(token_data, columns=['단어', '빈도수'])
dataFrame.to_csv(filename, encoding='UTF-8', index=False)
print(filename + ' 파일 저장 완료')

# 튜플(단어, 빈도수)을 저장하고 있는 리스트
wordList = list()

# 단어의 길이가 2이상이고, 빈도 수가 2이상인 항목만 추출하기
for word, bindo in token_data:
    if len(word) >= 2 and bindo >= 2:
        wordList.append((word, bindo))

print(wordList)

myFrame = pd.DataFrame(wordList, columns=['단어', '빈도수'])
print(myFrame.head())

print('상위 top 10개 막대 그래프')
barCount = 10 # 그리고자 하는 막대 개수
chartData = myFrame.set_index('단어').iloc[0:barCount]

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

chartData.plot(kind='bar', rot=10, grid=True, legend=False)

plt.title('빈도 ' + str(barCount) + '개 상위 단어', size=20)
plt.xlabel('주요 키워드', size=12)
plt.ylabel('빈도 수', size=12)

barFileName = dataInFolder + 'bar_chart.png'
plt.savefig(barFileName)
print(barFileName + ' 파일 저장됨')
# plt.show()

# 참조 url : https://amueller.github.io/word_cloud/index.html
print('단어 빈도를 이용한 워드 클라우드')

import numpy as np

# opencv 라이브러리도 같이 공부할 것
from PIL import Image # Python Image Library

# 워드 클라우드가 그려질 이미지
alice_color_file = dataInFolder + 'alice_color.png'
alice_color_array = np.array(Image.open(alice_color_file)) # 이미지 배열

# print(alice_color_array)

wordDict = dict(wordList) # 단어 사전

from wordcloud import WordCloud

fontName = 'malgun.ttf' # 글꼴

# myCloud : 워드 클라우드 객체
myCloud = WordCloud(font_path=fontName, mask=alice_color_array, background_color='white')

# 사전 정보(wordDict)로부터 빈도 수(frequencies)를 생성(generate)합니다.
myCloud = myCloud.generate_from_frequencies(wordDict)

# ImageColorGenerator : 컬러 이미지의 색상 톤을 유지하면서 워드 클라우드를 사용하고자 할때 사용합니다.
from wordcloud import ImageColorGenerator

colorGenerator = ImageColorGenerator(alice_color_array)

myCloud = myCloud.recolor(color_func=colorGenerator)

plt.figure(figsize=(16, 8)) # 큰 새로운 도화지 준비
plt.axis('off') # 그래프 테두리 없애기
plt.imshow(myCloud)

cloudFileName = dataInFolder + 'word_cloud.png'
plt.savefig(cloudFileName)
print(cloudFileName + ' 파일 저장됨')