tuple01 = ('김철수', 40, 50, 60)
tuple02 = ('박영희', 50, 60, 70)

mytuple = (tuple01, tuple02)
print(mytuple)

print('총 인원수 :', len(mytuple), '명', sep='')
print('평균 점수')

saram = mytuple[0][0]
jumsu = mytuple[0][1:]
hap = sum(jumsu)
mylen = len(jumsu)
average = hap/mylen

print(saram, ':', average, '점', sep='')

print('과목별 총점')

kor = mytuple[0][1] + mytuple[1][1]
print('국어 : ', kor, sep='')