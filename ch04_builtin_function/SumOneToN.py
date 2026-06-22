# SumOneToN.py
# 1부터 n까지의 총합을 구하는 프로그램
# 단, 음수 입력시 절대값으로 변경해야 합니다.
su = input('정수 1개 입력 : ') # 문자열로 인식
su = int(su)# 형변환

if su < 0:
    su = abs(su)

total = 0
for i in range(1, su+1):
    total += i

message = '%d부터 %d까지의 총합은 %d입니다.' % (1, su, total)
print(message)