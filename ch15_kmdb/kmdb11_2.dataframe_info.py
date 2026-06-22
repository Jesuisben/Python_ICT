import pandas as pd
myencoding = 'UTF-8' # 'CP949'  'UTF-8'  인코딩 문자열
filename = './../forOracle/kmdb_get_movie_list_100.csv'
dataframe = pd.read_csv(filename, encoding=myencoding)
print(type(dataframe))

print('행 색인 정보 확인')
print(dataframe.index)

print('열 색인 정보 확인')
print(dataframe.columns)

print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes.to_frame())

# 연속형, 범주형 데이터 언급하기
for column in dataframe.columns:
    print(column) # 컬럼 이름
    print(dataframe[column].unique()) # 컬럼별 unique한 항목 확인
    print('-'*30)

print('# 숫자 형식인 항목만 추출')
print('before count : ' + str(len(dataframe)))
# 문자열 컬럼 내부에는 str 키워드가 내재되어 있습니다.
# isdigit()는 숫자 형식의 문자열이면 True가 반환됩니다.
dataframe = dataframe[dataframe['movieCd'].str.isdigit()]
print('after count : ' + str(len(dataframe)))

print('\n장르 이름(repGenreNm)이 누락되지 않는 데이터만 추출')
print('before count : ' + str(dataframe.size))
# None, null, na 등을 결측치라고 합니다.
# notna = not na
# 결측치가 아닌 데이터는 True를 반환합니다.
dataframe = dataframe[dataframe['repGenreNm'].notna()]
print('after count : ' + str(dataframe.size))

# movieCd 열을 숫자형으로 변환(object → int64)
dataframe['movieCd'] = pd.to_numeric(dataframe['movieCd'])

print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes.to_frame())

print('\n제작 년도(prdtYear) 기초 통계량 확인')
prdtYear = dataframe['prdtYear']
print(type(prdtYear))
prdtYear.to_frame()

print('시리즈 요소 개수 확인 : ' + str(prdtYear.size))
print('prdtYear.shape : ' + str(prdtYear.shape))
print('len(prdtYear) : ' + str(len(prdtYear)))
# count()  함수는 결측치를 제외한 유효한 데이터 갯수
print('prdtYear.count() : ' + str(prdtYear.count()))

print('시리즈 데이터 타입 확인 : ' + str(prdtYear.dtype))

# nan은 데이터가 없거나 부정적인 뜻을 내포하고 있는 개념
print('누락된 데이터가 있나요? : ' + str(prdtYear.hasnans))
print('모든 항목이 unique한가요? : ' + str(prdtYear.is_unique))

print('prdtYear.quantile() : ' + str(prdtYear.quantile())) # 기본 값 : q=0.5(50%)
print('prdtYear.min() : ' + str(prdtYear.min()))
print('prdtYear.max() : ' + str(prdtYear.max()))
print('prdtYear.mean() : ' + str(prdtYear.mean())) # 평균
print('prdtYear.median() : ' + str(prdtYear.median())) # 중앙값
print('prdtYear.std() : ' + str(prdtYear.std())) # 표준 편차(STandard Devitation)
print('prdtYear.sum() : ' + str(prdtYear.sum()))

filename = './../forOracle/kmdb_get_movie_list_100_new.csv'
dataframe.to_csv(filename, index=False, encoding='UTF-8')
# movieTable.to_csv(filename, index=False, encoding='CP949')
print(filename + ' 파일이 저장되었습니다.')