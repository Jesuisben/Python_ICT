x = 3
y = 8
z = 4

result = x if x > y else y
result = result if result > z else z
print('큰 수 : %d' % result)

a = 3
b = 5
result = a-b if a > b else b-a
print('절대 값 : %d' % result)