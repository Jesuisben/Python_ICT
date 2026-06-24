# 매개변수 앞에 *적으면 튜플 타입이고 **적으면 사전 타입임

# 중요한 규칙!
# 1. 함수 생성시와 사용시 매개변수의 순서가 정해져있음
# (일반 -> *가변 위치 매개변수(args) -> **가변 키워드 매개변수(kwargs))
# 2. 하나의 함수의 매개변수에서 가변 위치 매개변수와 가변 키워드 매개변수는 하나씩만 넣을 수 있음
# 3. 가변 위치 매개변수나 가변 키워드 매개변수는 함수내에서 사용할때는 *나 **를 제거하고 사용함
def showData(category, *items, **keyword):
    print(f"category : {type(category)}")
    print(f"items : {type(items)}")
    print(f"keyword : {type(keyword)}")

    print('카테고리 이름 : %s' % category)
    print('가변 매개 변수 정보 출력')
    for element in items:
        print(element, end=' ')
    # end for
    print()

    print('키워드 매개 변수 정보 출력')
    for (key, value) in keyword.items():
        print('key=%s, value=%s' % (key, value))
    # end for

    print()

# showData 함수의 매개변수가 (일반, 가변 위치 변수, 가변 키워드 매개변수)로 구성이 되어있어서
# 1. 함수 사용시 맨 처음의 매개변수는 자동으로 일반으로 들어가게 됨
# 2. 나머지 매개변수 중에서 위치 기반 변수들은 모두 가변 위치 변수로 들어가고 튜플로 생성됨
# 3. 나머지 매개변수 중에서 키워드 기반 변수들은 가변 키워드 매개변수에 들어가게 되고 사전으로 생성됨
showData('과일', '바나나', '사과', '오렌지', 파인애플=100, 귤=30)
showData('커피', '아메리카노', '카페라떼', '바닐라라떼', '디카페인커피')


# # ArbitraryArgument01.py
# # 가변 매개 변수는 매개 변수의 개수가 딱히 정해져 있지 않는 매개 변수를 의미합니다.
# # 매개 변수 이름에 *이 명시되어 있으면 가변 매개 변수가 되며, 내부에서는 tuple 형식으로 처리됩니다.
#
# # 키워드 매개 변수는 ** 기호를 사용합니다.
# # 내부적으로 dict 형식으로 처리됩니다.
# # 함수 호출시 key=value의 형식으로 호출합니다.
#
# def showData(category, *items, **keyword):
#     print('타입 : %s' % type(category))
#     print('카테고리 이름 : %s' % category)
#     print('type(items) : %s' % type(items))
#     print('type(keyword) : %s' % type(keyword))
#
#     print('가변 매개 변수 정보 출력')
#     for element in items:
#         print(element, end=' ')
#     # end for
#     print()
#
#     print('키워드 매개 변수 정보 출력')
#     for (key, value) in keyword.items():
#         print('key=%s, value=%s' % (key, value))
#     # end for
#
#     print()
# # end def
#
# showData('과일', '바나나', '사과', '오렌지', 파인애플=100, 귤=30)
# showData('커피', '아메리카노', '카페라떼', '바닐라라떼', '디카페인커피')
