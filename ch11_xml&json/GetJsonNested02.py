import json

dataIn = "../dataIn/"

filename = dataIn + "HumanData02.json"

with open(filename, "r", encoding="UTF-8") as myfile:
    result = myfile.read()
    myjson = json.loads(result)
    print(f"원본 JSON 타입 : {type(myjson)}")
    print(f"요소 갯수 : {len(myjson)}")

    mylist = []

    for item in myjson:
        name = myjson[item]["basic"]["name"]
        origin = myjson[item]["basic"]["origin"]
        roast = myjson[item]["basic"]["roast"]

        brand = myjson[item]["store"]["brand"]
        branch = myjson[item]["store"]["branch"]
        last_brewed = myjson[item]["store"]["last_brewed"]
        status = myjson[item]["store"]["status"]

        if name == "아메리카노":
            recipe = f"레시피 : 물의 양->{myjson[item]['recipe']['water']}/에스프레소샷->{myjson[item]['recipe']['espresso_shot']}"
        elif name == "카페라떼":
            recipe = f"레시피 : 우유량->{myjson[item]['recipe']['milk']}/에스프레소샷->{myjson[item]['recipe']['espresso_shot']}"
        else:
            recipe = f"레시피 : 우유량->{myjson[item]['recipe']['milk']}/에스프레소샷->{myjson[item]['recipe']['espresso_shot']}/milk->{myjson[item]['recipe']['chocolate']}"

        mylist.append((name, origin, roast, brand, branch, last_brewed, status, recipe))


print(mylist)


# import json
#
# filename = 'HumanData02.json'
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
# coffee_list = []
#
# recipe_dict ={"milk": "우유량", "espresso_shot": "에스프레소샷", "chocolate": "초콜릿", "water": "물의 양"}
#
# for key in jsondata:
#     # print(f'{key} ')
#
#     # 기본 정보
#     name = jsondata[key]['basic']['name']
#     origin = jsondata[key]['basic']['origin']
#     roast = jsondata[key]['basic']['roast']
#
#     # 레시피 정보
#     recipe = jsondata[key]['recipe'] # 결과는 사전
#     recipe_comment = '레시피 : '
#     for rcpkey in recipe.keys():
#         recipe_comment += f'{recipe_dict[rcpkey]}→{recipe[rcpkey]}/'
#     # end for
#
#     recipe_comment = recipe_comment[:-1] # 마지막 한글자 지우기
#
#     # 매장 정보
#     brand = jsondata[key]['store']['brand']
#     branch = jsondata[key]['store']['branch']
#     last_brewed = jsondata[key]['store']['last_brewed']
#     status = jsondata[key]['store']['status']
#
#     print(f'{name},{origin},{roast},{brand},{branch},{last_brewed},{status},{recipe_comment}')
#
#     myTuple = (name, origin, roast, brand, branch, last_brewed, status, recipe_comment)
#     coffee_list.append(myTuple)
#     # end for
#
# print(coffee_list)