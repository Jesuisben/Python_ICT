def namePrint(name, age):
    message = '\'{}\'님의 나이는 {}세입니다.'.format(name, age)
    print(message)
# end def

def sayHello(message, n = 10):
    for idx in range(n):
        print(message)
    print()
# end def

# 넘겨진 문자열을 / 기호로 분리한 후 list를 반환하는 함수
def character_split(mystring) :
    # 함수로 만들때는 매개변수가 어떤 타입인지 모르니까
    # 그 타입에 해당하는 함수가 추천되지는 않는듯
    return mystring.split("/")

# 넘겨진 list를 특정한 기호(symbol)와 함께 사용하여 문자열을 반환해주는 함수
def list_join(mylist, symbol) :
    return str(symbol).join(mylist)