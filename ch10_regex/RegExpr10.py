import  re
'''
도전 문제)	Regular_Expression_05_With_FileIO.py
reg_mem.txt 파일을 읽어서, 다음과 같은 순서대로 된 데이터를 만들어 보세요.
아이디, 이름, 나이, 성별, 생일
'''
def getBirth(birth):
    regex = '[년월-]' # 바꿀 단어들
    pattern = re.compile(regex)
    newbirth01 = pattern.sub('/', birth)

    regex = '[일]'  # 바꿀 단어들
    pattern = re.compile(regex)
    newbirth01 = pattern.sub('', newbirth01)
    # print('[', newbirth01, ']', sep='')

    regex = '/'
    pattern = re.compile(regex)
    newbirth02 = pattern.split(newbirth01)
    if len(newbirth02) == 3 :
        newbirth02 = newbirth02[0] + '/' + newbirth02[1].zfill(2) + '/' + newbirth02[2].zfill(2)
    else :
        newbirth02 = newbirth02[0][0:4] + '/' + newbirth02[0][4:6] + '/' + newbirth02[0][6:]

    # print(newbirth02)
    return newbirth02

myfile = open(file='members.txt', mode='r', encoding='utf-8')

mylist = myfile.readlines()
newlist = [item.strip() for item in mylist]
# print(newlist)
myfile.close()

totallist = []
for oneline in newlist :
    regex = ','
    pattern = re.compile(regex)
    result = pattern.split(oneline)
    print(result)  # list

    id, name, _age = result[0], result[1], int(result[2][0:2])
    if _age >= 50:
        age = 2024 - (1900 + _age)
    else:
        age = 2024 - (2000 + _age)

    _gender = result[2][7:8] # 성별
    if _gender in ['1', '3']:
        gender = '남자'
    elif _gender in ['2', '4']:
        gender = '여자'

    birth = getBirth(result[3])

    mytuple = (id, name, age, gender, birth)
    totallist.append(mytuple)
    print('#'*20)
# end for

print(totallist)

newfile = open(file='mem_result.txt', mode='w', encoding='utf-8')

for sometuple in totallist :
    data = sometuple[0] + ',' + sometuple[1] + ',' + str(sometuple[2]) + ',' +sometuple[3] + ',' +sometuple[4] + '\n'
    newfile.write(data)
# end for

newfile.close()
print('finished')