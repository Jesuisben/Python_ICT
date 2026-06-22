# ArbitraryArgument01.py
# 가변 매개 변수는 매개 변수의 개수가 딱히 정해져 있지 않는 매개 변수를 의미합니다.
# 매개 변수 이름에 *이 명시되어 있으면 가변 매개 변수가 되며, 내부에서는 tuple 형식으로 처리됩니다.

# 키워드 매개 변수는 ** 기호를 사용합니다.
# 내부적으로 dict 형식으로 처리됩니다.
# 함수 호출시 key=value의 형식으로 호출합니다.

def showData(category, *items, **keyword):
    print('타입 : %s' % type(category))
    print('카테고리 이름 : %s' % category)
    print('type(items) : %s' % type(items))
    print('type(keyword) : %s' % type(keyword))

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
# end def

showData('과일', '바나나', '사과', '오렌지', 파인애플=100, 귤=30)
showData('커피', '아메리카노', '카페라떼', '바닐라라떼', '디카페인커피')
