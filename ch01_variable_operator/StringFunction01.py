# 문자열 함수 실습
mystring = 'Hello python!'

# len() 함수는 요소의 개수를 구해 주는 파이썬 내장 함수입니다.
print('길이 : %d' % len(mystring))
# count() 함수 : 그 문자열의 매개변수에 속하는 글자가 몇개 있는지 count해줌
print('\'o\' 개수 몇개 ? %d' % mystring.count('o'))

# 알파벳 e를 첫 색인부터 검색
# find() 함수 : 그 문자열의 매개변수에 속하는 글자의 첫번째 인덱스 번호를 반환함
print('검색 위치 01 : %d' % mystring.find('e'))

# 알파벳 o를 6번째 색인부터 검색
# find("찾을 단어", 숫자) : 인덱스 번호 (숫자)부터 쭉 찾아서 "찾을 단어"가 나오면 인덱스 번호를 반환함
print('검색 위치 02 : %d' % mystring.find('o', 6))

# 이름이 r로 시작되는 함수의 r은 right를 의미합니다.
# 알파벳 l를 끝 색인부터 검색
# rfind() 함수 : 오른쪽에서부터 해당 단어를 찾아서 나오는 첫번째 해당 단어의 인덱스 번호를 반환함
print('검색 위치 03 : %d' % mystring.rfind('l'))

# replace(대체될단어, 대체할단어) 함수 : 해당 문자열 내에 속한 단어를 새로운 단어로 대체함
print('문자열 치환 01 : %s' % mystring.replace('l', 't'))

# replace(대체될단어, 대체할단어, 숫자) 함수 : 해당 문자열 내에 속한 단어를 새로운 단어로 숫자만큼 대체함
# 숫자가 1이니까 앞에서 부터 "l"인 단어를 't'로 한번만 대체함 (첫번째꺼만 대체)
print('문자열 치환 02 : %s' % mystring.replace('l', 't', 1))

mystring = '   가나  다라    '

# strip() 함수의 작업 대상은 '공백'이 기본 값입니다.
# strip() 함수 : 공백 제거에 주로 이용 (중요!) (나중에 크롤링 같은 것에서 자주 사용됨)
# 양쪽 공백 다 제거
print('공백 제거 01 : [%s]' % mystring.strip())

# 오른쪽 공백 제거
print('공백 제거 02 : [%s]' % mystring.rstrip())

# 이름이 l로 시작되는 함수의 l은 left를 의미합니다.
# 왼쪽 공백 제거
print('공백 제거 03 : [%s]' % mystring.lstrip())

# strip() 함수에 매개변수가 들어가면 그 매개변수를 다 제거함
mystring = 'xxxHelloxxx'
print('공백 제거 04 : [%s]' % mystring.strip('x'))

# lstrip () 함수는 해당 매개변수에 해당하는 단어를 문자열에서 왼쪽 부분만 제거함
mystring = 'xxxHelloxxx'
print('공백 제거 05 : [%s]' % mystring.lstrip('x'))

mystring = 'hello python!'
print('대문자 : [%s]' % mystring.upper())
print('소문자 : [%s]' % mystring.lower())

# capitalize() 함수 : 해당 문자열의 첫번째 글자만 대문자로 바꿈
print('첫 글자만 대문자 : [%s]' % mystring.capitalize())

# split() 함수의 기본 동작은 '공백'을 대상으로 분리하여 list를 만들어 줍니다.
# list는 순서가 있는 자료 구조입니다.
# split() 함수 : 매개변수가 없으면 공백을 기준으로, 매개변수가 있으면 매개변수를 기준으로 문자열을 나눔
print('문자열 분리 01 : [%s]' % mystring.split())

# 매개변수 "/"여서 "/"를 기준으로 문자열을 나눔
mystring = '아메리카노/카페라떼/카푸치노'
print('문자열 분리 02 : [%s]' % mystring.split('/'))

# bool(ean) 타입의 값이 반환됨
mystring = 'hello.xls'
print('H로 시작하나요 ? [%s]' % mystring.startswith('H'))
print('xls로 끝이 나나요 ? [%s]' % mystring.endswith('.xls'))

# 가전 제품 리스트
# '문자1'.join(반복객체) : '반복객체'의 요소들을 결합하여 한개의 문자열로 만들어 주세요.
# 중간 구분자로 '문자1'을 사용해 주시구요.

mylist = ['삼성', '엘지', '대우']
# 위의 배열을 join을 사용하면 한개의 문자열로 만들 수 있음
# 문자열을 만들때 그 배열을 요소의 구분자를 문자1.join할때의 문자1로 연결해서 한개의 문자열로 생성
print('join 함수 : [%s]' % '#'.join(mylist))

# 인덱싱 (매우중요)
mystring = 'Korea'
munja = mystring[2]
print('문자 : [%c]' % munja)

print('대문자인가요 ? [%s]' % munja.isupper())
print('소문자인가요 ? [%s]' % munja.islower())
# isdigit() : 문자열이 숫자로만 구성되어있는지 확인하는 함수
# bool(ean) 타입으로 반환함
print('숫자인가요 ? [%s]' % munja.isdigit())

# ord() 함수 : 매개변수의 아스키 코드 정수를 반환하는 함수
print('아스키 코드 : [%d]' % ord(munja))
print('소문자 a : [%d]' % ord('a'))
print('대문자 A : [%d]' % ord('A'))