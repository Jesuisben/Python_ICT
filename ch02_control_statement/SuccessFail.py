mid = int(input("중간 고사 점수 : "))
fin = int(input("기말 고사 점수 : "))

jumsu = mid * 0.4 + fin * 0.6

if jumsu >= 70:
    message = "Pass"
else:
    message = "Fail"

print('중간 고사 점수 : {}'.format(mid))
print('기말 고사 점수 : {}'.format(fin))
print('점수 : {}'.format(jumsu))
print('합격 여부 : {}'.format(message))
