import json

coffee_menu = {
    "americano": {
        "size": {
            "small": 2000,
            "medium": 2500,
            "large": 3000
        },
        "extra_shot": {
            "yes": 600,
            "no": 0
        },
        "whipped_cream": {
            "yes": 300,
            "no": 0
        }
    },
    "latte": {
        "size": {
            "small": 3300,
            "medium": 3600,
            "large": 3900
        },
        "extra_shot": {
            "yes": 400,
            "no": 0
        },
        "whipped_cream": {
            "yes": 200,
            "no": 0
        }
    },
    "cappuccino": {
        "size": {
            "small": 4000,
            "medium": 5000,
            "large": 6000
        },
        "extra_shot": {
            "yes": 700,
            "no": 0
        },
        "whipped_cream": {
            "yes": 400,
            "no": 0
        }
    }
}


print('dumps 함수는 사전을 문자열 형식으로 변형해 줍니다.')
# ensure_ascii=False : 문자열을 이스케이프하지 않고, 한글을 그대로 보여 주고자 할 때 사용합니다.
coffeeString = json.dumps(coffee_menu, ensure_ascii=False, indent=4, sort_keys=True)
print(type(coffeeString))
# print(coffeeString)

coffeeJson = json.loads(coffeeString)

print('품목 개수 : %d' % len(coffeeJson))

coffeeList = []

for item in coffeeJson:
    name = item
    # print(coffeeJson[item])
    size_sm = coffeeJson[item]['size']['small']
    size_md = coffeeJson[item]['size']['medium']
    size_lg = coffeeJson[item]['size']['large']
    shot_price = coffeeJson[item]['extra_shot']['yes']
    whip_price = coffeeJson[item]['whipped_cream']['yes']
    one_coffee = (name, size_sm, size_md, size_lg, shot_price, whip_price)

    coffeeList.append(one_coffee)
# end for

print('열거된 내용은 품명, 사이즈(소), 사이즈(중), 사이즈(대), 샷추가_가격, 휘핑 추가 가격 순입니다.')
print(coffeeList)