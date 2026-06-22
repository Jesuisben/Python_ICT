print('두 수의 곱셈을 반환하는 람다 함수 mul_lambda 만들기')
mul_lambda = lambda a, b: a * b
result = mul_lambda(14, 5)
print('람다 방식 01 : %d' % result)

print('1부터 10까지의 정수 중 3의 배수가 아닌 수의 비율)')
somedata = [idx for idx in range(1, 11)]
three_bae = lambda a: a % 3 != 0
result = [three_bae(su) for su in somedata]
print(result)
print(sum(result) / len(result))

print('1부터 10까지의 정수 중 3의 배수가 아닌 수만 출력하기')
somedata = [idx for idx in range(1, 11)]
result = list(filter(three_bae, somedata))
print(result)

print('리스트 요소 각각에 100을 더한 결과를 출력해 보세요')
somedata = [20, 50, 70]
map_lambda = lambda num: num+100
result = list(map(map_lambda, somedata))
print(result)