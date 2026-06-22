def max(x, y, z):
    result = x if x > y else y
    result = result if result > z else z
    return result
# end def


def min(x, y, z):
    result = x if x < y else y
    result = result if result < z else z
    return result
# end def


x = 12
y = 8
z = 20
result = min(x, y, z)
print("최소 : %d" % result)

result = max(x, y, z)
print("최대 : %d" % result)