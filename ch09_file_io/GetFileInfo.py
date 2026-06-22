import os

mydict = {} # 총 점수를 위한 사전

filepath = './'
for year in range(2015, 2018):
    # filename : 해당 년도의 텍스트 파일
    filename = filepath + 'somefile' + str(year) + '.txt'
    #print(filename)
    
    # exists : 존재 여부를 알려 주는 함수
    isexist = os.path.exists(filename)
    #print(isexist) 
    
    if isexist == True:
        myfile = open(filename, 'rt', encoding='utf-8')

        # mylines : 파일 1개의 행수
        mylines = myfile.readlines()
        for oneline in mylines:
            data = oneline.split(',')
            name = data[0]
            jumsu = int(data[1])

            if name in mydict.keys():
                mytuple = mydict[name]

                # mydict[키이름] = (누적된점수 + 새로운점수, 누적카운트 + 1)
                mydict[name] = (mytuple[0] + jumsu, mytuple[1] + 1)

            else: # value는 (점수누적, 카운트누적)
                mydict[name] = (jumsu, 1)
            # end inner if
        # end inner for
        #print('-' * 20)
        myfile.close()
    # end outer if
# end outer for

print('-' * 30)
for key, value in mydict.items():
    print('이름 : %s, 누적 점수 : %s, 누적 카운트 : %s' %(key, value[0], value[1]))
    
print('finished')