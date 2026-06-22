begin = int(input('시작 단수 입력 : '))
end = int(input('끝 단수 입력 : '))

# 이전 방식의 swap 기법
'''
if begin > end:
    imsi = begin
    begin = end
    end = imsi
'''

# python에서는 다음과 같이 처리하면 됩니다.
begin, end = end, begin # tuple의 특징

for i in range(begin, end+1):
    for j in range(1, 10):
        message = '%2d * %2d = %2d'
        print(message % (i, j, (i * j)), end='')
    # end inner for
    print()
# end outer for