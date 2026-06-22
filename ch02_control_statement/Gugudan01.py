# 구구단 프로그램
for i in range(2, 10):  # row(행)
    for j in range(1, 10):  # column(열)
        message = '%2d * %2d = %2d'
        print(message % (i, j, (i * j)), end='')
    # end inner for
    print()  # 구구단 한개의 단이 끝날 때 엔터
# end outer for