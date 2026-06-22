import  re
from datetime import datetime

'''
도전 문제)
members.txt 파일을 읽어서, 다음과 같은 순서대로 된 데이터를 만들어 보세요.
아이디, 이름, 나이, 성별, 생일
'''
def getBirth(birth):
    regEx = '[년월-]' # 바꿀 단어들
    pattern = re.compile(regEx)
    sub_birth = pattern.sub('/', birth)

    regEx = '[일]'  # 바꿀 단어들
    pattern = re.compile(regEx)
    sub_birth = pattern.sub('', sub_birth)
    # print('[', sub_birth, ']', sep='')

    regEx = '/'
    pattern = re.compile(regEx)
    new_birth = pattern.split(sub_birth)
    if len(new_birth) == 3 :
        new_birth = new_birth[0] + '/' + new_birth[1].zfill(2) + '/' + new_birth[2].zfill(2)
    else :
        new_birth = new_birth[0][0:4] + '/' + new_birth[0][4:6] + '/' + new_birth[0][6:]

    # print(new_birth)
    return new_birth
# end def getBirth

myfile = open(file='members.txt', mode='r', encoding='utf-8')

mylist = myfile.readlines()
newlist = [item.strip() for item in mylist]
# print(newlist)
myfile.close()

current_year = datetime.now().year  # 현재 연도를 가져옴 (예: 2025)

totallist = []
for oneline in newlist :
    regEx = ','
    pattern = re.compile(regEx)
    result = pattern.split(oneline)
    print(result)  # list

    id, name, _age = result[0], result[1], int(result[2][0:2])
    if _age >= 50:
        age = current_year - (1900 + _age)
    else:
        age = current_year - (2000 + _age)

    _gender = result[2][7:8] # 성별
    if _gender in ['1', '3']:
        gender = '남자'
    elif _gender in ['2', '4']:
        gender = '여자'

    birth = getBirth(result[3])

    mytuple = (id, name, str(age), gender, birth)
    totallist.append(mytuple)
    print('#'*20)
# end for

print(totallist)

newfile = open(file='mem_result.txt', mode='w', encoding='utf-8')

for sometuple in totallist :
    data = ','.join(sometuple)
    newfile.write(data + '\n')
# end for

newfile.close()