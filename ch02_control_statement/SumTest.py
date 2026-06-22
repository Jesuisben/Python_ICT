sumA, sumB, sumC = 0, 0, 0

for i in range(1, 11):
    if i % 3 == 0:
        sumA += i
    else:
        if i >= 5:
            if i != 8:
                sumB += i
        else:
            sumC += i
    # end if
# end for

print("sumA : %d" % sumA)
print("sumB : %d" % sumB)
print("sumC : %d" % sumC)