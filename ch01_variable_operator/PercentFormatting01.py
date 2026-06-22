# % 포맷 코드 : %d(decimal), %s(string), %c(character)
# %f(float)의 기본 값은 소수점 6자리까지 표시됩니다.
# %m.nf(float) : m과 n은 정수이고, m은 전체 자리수, n은 소수점 자리수입니다.

name = "김철수"
age = 30
height = 175.3456789
address = '마포'

print('이름 : %s' % name) # %s : 치환될 데이터 (% name이 %s로 치환됨)
print('나이 : %d' % age) # %d (decimal : 10진수)
print('키01 : %.3f' % height) # %.3f : 소수점 3번째까지 출력
# %10.4f : 소수점 앞자리 10번째까지, 소수점 아래 4번째까지 출력
# %에 적힌 숫자가 양수여서 우측정렬이기도 함
print('키02 : [%10.4f]' % height)
print('주소 : %s' % address)

# 포맷 코드들이 여러개 있으면 순서에 맞게 치환됨 / ()를 써주고 그 안에 치환된 변수 넣어줌
# 참고로 첫번째는 1번째가 아니고 0번째임
message = '이름은 %s이고, 나이는 %d살입니다.'
print(message % (name, age))

su = 2
bread = '단팥빵'
message = '나는 배고파서 %s %d개를 먹었습니다.'
print(message % (bread, su))

su01 = 3
su02 = 5
message = '%d 더하기 %d는 %d입니다.'
print(message % (su01, su02, (su01+su02)))

# %에 숫자는 f가 아니여도 넣을 수 있음 (공간 확보 및 공간확보 방향(정렬))
hello = '안녕' # 기호 [와 ]는 편의상 테두리 임을 알려 주는 역할
message = '[%10s]' % hello # 숫자가 양수이면, 오른쪽 정렬
print(message)

message = '[%-10s]' % hello # 숫자가 음수이면, 왼쪽 정렬
print(message)