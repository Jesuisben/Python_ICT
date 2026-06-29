import json

dataIn = "../dataIn/"

filename = dataIn + "HumanData01.json"

# json (JavaScript Object Notation) : 자바스크립트 객체 표기법
# json이 텍스트 파일이여서 파일 생성, 수정 및 읽어오기할때와 같은 문법 사용가능
with open(filename, "rt", encoding="UTF-8") as myfile:
    # read() : 문자열로 반환함
    mystring = myfile.read()

    # load는 파일 객체에서 직접 읽어서 사전 타입으로 변환
    # jsondata = json.load(myfile)  # 파일 객체를 직접 넘김 (myfile.read()가 필요없음)

    # loads : 문자열을 사전 타입으로 변환
    # 사전 타입으로 반환함
    jsondata = json.loads(mystring)

print(f"원본 json 타입 : {type(jsondata)}")
print(f"요소 개수 : {len(jsondata)}")
# print(jsondata)

# 데이터를 담을 리스트 생성
human_list = []

# String인 json을 사전 타입으로 가져와서 값이자 하위 키인 데이터에 접근 가능함
for key in jsondata:
    # 기본 정보
    name = jsondata[key]['name']
    age = jsondata[key]['age']

    # 집주소 정보
    street = jsondata[key]['location']['address']['street']
    city = jsondata[key]['location']['address']['city']
    gu = jsondata[key]['location']['address']['gu']

    # 연락처 정보
    contact = jsondata[key]['contact'] # 결과는 사전
    mobile = contact['mobile']
    email = contact['email']

    # 직업 정보
    job_title = jsondata[key]['job']['title']
    company_name = jsondata[key]['job']['company']['name']
    company_location = jsondata[key]['job']['company']['location']

    # skill 정보
    skills = jsondata[key]['skills']
    # skills는 리스트 타입인데 '%'.join(skills)를 이용해서 "%"를 구분자로 문자열로 합침
    myskill = '%'.join(skills)

    # print(f'{name},{age},{street},{city},{gu},{mobile},{email},{job_title},{company_name},{company_location},{myskill}')

    myTuple = (name, age, street, city, gu, mobile, email, job_title, company_name, company_location, myskill)
    human_list.append(myTuple)
    # end for

print(human_list)


# import json
#
# filename = 'HumanData01.json'
#
# with open(filename, 'rt', encoding='UTF-8') as myfile:
#     mystring = myfile.read()
#     jsondata = json.loads(mystring)
# # end with
#
# print(f'원본 JSON 타입 : {type(jsondata)}')
# print(f'요소 갯수 : {len(jsondata)}')
# print()
# # print(jsondata)
#
# human_list = []
#
# for key in jsondata:
#     # 기본 정보
#     name = jsondata[key]['name']
#     age = jsondata[key]['age']
#
#     # 집주소 정보
#     street = jsondata[key]['location']['address']['street']
#     city = jsondata[key]['location']['address']['city']
#     gu = jsondata[key]['location']['address']['gu']
#
#     # 연락처 정보
#     contact = jsondata[key]['contact'] # 결과는 사전
#     mobile = contact['mobile']
#     email = contact['email']
#
#     # 직업 정보
#     job_title = jsondata[key]['job']['title']
#     company_name = jsondata[key]['job']['company']['name']
#     company_location = jsondata[key]['job']['company']['location']
#
#     # skill 정보
#     skills = jsondata[key]['skills']
#     myskill = '%'.join(skills)
#
#     # print(f'{name},{age},{street},{city},{gu},{mobile},{email},{job_title},{company_name},{company_location},{myskill}')
#
#     myTuple = (name, age, street, city, gu, mobile, email, job_title, company_name, company_location, myskill)
#     human_list.append(myTuple)
#     # end for
#
# print(human_list)