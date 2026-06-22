import json 

def get_Json_Data():
    filename = '김주혁_naver_news.json'
    myfile = open(filename, 'rt', encoding='utf-8')
    myfile = myfile.read()
    jsonData = json.loads( myfile )

    for oneitem in jsonData :
        title = oneitem['title']
        description = oneitem['description']

        print('\n타이틀 : %s' % (title))
        print('설명 : %s' % (description))
    print('-' * 40)

get_Json_Data()