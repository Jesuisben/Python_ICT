# mylist01 = [ x*y for x in range(2, 10) for y in range(1, 10)]
# print(mylist01)
# print('-'*30)

print('-- 출력1 --')
for idx in range(1, 6):
    for jdx in range(1, 6):
        print( jdx, end = ' ')
    print()
print('-' * 50)

print('-- 출력2 --')
for idx in range(1, 6):
    for jdx in range(1, 6):
        print( idx, end = ' ')
    print()
print('-' * 50)

print('-- 출력3 --')
for idx in range(1, 6):
    for jdx in range(1, 6):
        print( jdx + idx - 1, end = ' ')
    print()
print('-' * 50)

print('-- 출력4 --')
for idx in range(1, 6):
    for jdx in range(9, 4, -1):
        print( jdx - idx + 1 , end = ' ')
    print()
print('-' * 50)