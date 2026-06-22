dan = int(input('몇단 출력? '))

i = 1
while i < 10:
    message = '%d * %d = %2d'
    print(message % (dan, i, (dan*i)))
    i += 1