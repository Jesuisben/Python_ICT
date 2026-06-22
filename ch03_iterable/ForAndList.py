examdata = [90, 30, 65, 45, 80] # 시험 점수 리스트

print('요소 1개씩 출력하기')
for jumsu in examdata:
    print('%s ' % jumsu, end='')
print()

print('\nrange() 함수 사용하기')

# idx는 색인 번호, examdata[idx]는 해당 요소의 값을 의미합니다.
# 점수가 60점 이상이면 합격 처리합니다.
for idx in range(len(examdata)):
    if examdata[idx] >= 60:
        print('%d번째 응시자 %3d점 : %s' % (idx+1, examdata[idx], '합격'))
    else:
        print('%d번째 응시자 %3d점 : %s' % (idx+1, examdata[idx], '불합격'))

print('\n합격자만 출력하기')
# 불합격자는 continue 구문을 이용하여 처리합니다.
for idx in range(len(examdata)):
    if examdata[idx] >= 60:
        print('%d번째 응시자 %3d점 : %s' % (idx+1, examdata[idx], '합격'))
    else:
        continue # 현시점의 하단 코드는 무시하고, 다음 step으로 이동하기 위한 구문
        print('%d번째 응시자 %3d점 : %s' % (idx + 1, examdata[idx], '불합격'))

'''
문자열을 공백으로 분리하여 list를 생성합니다.
해당 리스트의 요소 번호에 대하여 홀/짝으로 분리하여 각각 소/대문자로 표현해봅니다.
리스트 요소의 모든 문자열을 결합하되, 중간 구분자로 #을 붙여 보도록 합니다.

최종 목표 문자열 : LIEF#is#AN#egg 
'''
mystring = 'life is an egg'
sentences = mystring.split()
print(type(sentences))
print('before list : %s' % sentences)

for idx in range(len(sentences)):
    if idx % 2 == 0:
        sentences[idx] = sentences[idx].upper()
    else:
        sentences[idx] = sentences[idx].lower()
# end for

print('after list : %s' % sentences)

# '끼워넣을문자열'.join(작업대상)
joinSentence = '#'.join(sentences)
print('Final Result : %s' % joinSentence )