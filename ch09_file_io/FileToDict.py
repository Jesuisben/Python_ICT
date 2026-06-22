print('파일 열기')
filename = 'mem.txt'

myfile = open(file=filename, mode='r', encoding='UTF-8')

mydict = {}

while True:
    line = myfile.readline().strip()
    if not line:
        break
    datalist = line.split(',')
    mydict[datalist[0]] = int(datalist[1])

myfile.close()
print(mydict)