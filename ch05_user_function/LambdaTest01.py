# LambdaTest01.py
# 두 수의 합을 구해 주는 함수 선언
def hap(x, y):
    return x + y


x, y = 14, 5
result = hap(x, y)
print('일반 함수 방식 : %d' % result)

# 람다 함수는 익명 함수라고 하며, 한줄로 간결하게 작성하고자 할 때 사용하는 기법입니다.
# lambda arguments: expression
# arguments는 매개 변수, expression은 반환될 수식입니다.
hap_lambda = lambda a, b: a + b

result = hap_lambda(10, 20)

print('람다 방식 01 : %d' % result)

print('제곱 수 구하기(람다 함수 + 리스트 컴프리헨션)')
somedata = [2, 5, 7]
pow_lambda = lambda a: a ** 2
result = [pow_lambda(su) for su in somedata]
print(result)

print('관계 연산자와 람다 함수(3의 배수의 비율)')
somedata = [idx for idx in range(1, 11)]
three_bae = lambda a: a % 3 == 0
result = [three_bae(su) for su in somedata]
print(result)
print(sum(result) / len(result))

# 람다 함수는 주로 map(), filter(), sorted() 등의 함수와 함께 사용이 됩니다.
# filter(function, iterable) : iterable 항목 중에서 function 조건에 부합하는 데이터만 필터링해 줍니다.
print('리스트 요소 중에서 3의 배수만 출력하기')
somedata = [idx for idx in range(1, 11)]
result = list(filter(three_bae, somedata))
print(result)

# map(function, iterable) : iterable 항목들을 function라는 동작시켜 새로운 데이터를 만들어 내는 함수입니다.
print('리스트 요소 각각의 값에 3을 곱한 결과')
somedata = [2, 5, 7]
map_lambda = lambda num: 3*num

# somedata의 각 요소들을 map_lambda라는 람다 함수에 적용시켜 주세요.
result = list(map(map_lambda, somedata))
print(result)