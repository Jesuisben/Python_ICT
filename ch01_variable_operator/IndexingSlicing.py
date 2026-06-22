# 인덱싱과 슬라이싱
# 문자열의 일부를 선택하거나 추출해 내는 기법을 의미합니다.

# sequence : 문자열, 리스트, 튜플
str1 = 'Hello Korea'

# 인덱싱 : 대괄호 기호와 색인(index)을 이용하여 요소를 추출하는 기능
print(str1[0])
print(str1[1], str1[6])

# 음수는 -0이 없어서 맨 뒤 글자는 -1임
print(str1[-3]) # 음수는 뒤에서부터 카운터

# 'KHa'가 출력되도록 인덱싱해보세요.
# sep='' : 구분자는 없음 (원래 디폴트는 \n)
print(str1[6], str1[0], str1[10], sep='')

# 슬라이싱 : 전체에서 일부를 추출하는 기능
# from:to:step ==> 시작인덱스:끝인덱스:증감치
# step의 증감치로 from <= 슬라이싱 < to 를 추출합니다.
# from은 0, to는 전체 길이, step은 1의 기본 값을 가집니다.
print(str1[0:5])
print(str1[:5])
print(str1[0:5:2]) # 0, 2, 4인 인덱스를 가져옴

# 인덱싱과 슬라이싱 차이 : 인덱싱은 한 글자밖에 못가져오고 슬라이싱은 여러 글자를 가져올 수 있음

# 주민 등록 번호 앞자리와 뒤자리를 출력 및 성별도 확인해 보세요.
ssn = '881120-1234567'
apos = ssn[0:6] # 앞자리
print('주민 번호 앞자리 : %s' % apos)

dpos = ssn[7:]
print('주민 번호 뒷자리 : %s' % dpos)

gender = ssn[7]

if gender == '1' or gender == '3':
    print('남자')
else:
    print('여자')

today = '20240227rainy'

# 2024년 02월 27일의 날씨는 rainy입니다.
year = today[0:4]
month = today[4:6]
day = today[6:8]
weather = today[8:]

myformat = '%s년 %s월 %s일의 날씨는 \'%s\'입니다.'
print(myformat % (year, month, day, weather))