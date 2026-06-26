dataIn, dataOut = "../dataIn/", "../dataOut/"

# JumsuCheck02.py
# jumsu.txt 파일을 읽어서, '이름/성별/총점/평균' 형식으로 result.txt 파일에 기록하는 프로그램을 작성해 보세요.
myencoding = 'UTF-8'

source = open(file= dataIn + 'jumsu.txt', mode='rt', encoding=myencoding) # 읽어올 파일

destination = open(file= dataOut + 'result.txt', mode='wt', encoding=myencoding) # 신규 생성할 파일

# readlines() 함수를 써도 결국 "한줄씩" 여러줄을 가져오는 것이여서 \n이 포함되어서 읽어옴
# 그래서 .strip() 함수를 사용함
students = [item.strip() for item in source.readlines()]
print(students)

for bean in students:
    human = bean.split(',')
    # print(human)
    name = human[0]
    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])
    _gender = human[4].upper()

    total = kor + eng + math
    average = total / 3.0

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    # '이름/성별/총점/평균' 형식
    sentences = '%s/%s/%.1f/%.2f\n' % (name, gender, total, average)
    print(sentences)

    destination.write(sentences)
# end for

source.close()
destination.close()
print('작업이 완료되었습니다.')