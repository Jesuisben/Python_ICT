mylist = []

def min01(x, y, z):
    mylist.append(x)
    mylist.append(y)
    mylist.append(z)
    print(f"최소값은 : {min(mylist)}")

def max01(x, y, z):
    mylist.append(x)
    mylist.append(y)
    mylist.append(z)
    print(f"최대값은 : {max(mylist)}")

min01(3, 8, 5)
max01(3, 8, 5)


# def max(x, y, z):
#     result = x if x > y else y
#     result = result if result > z else z
#     return result
# # end def
#
#
# def min(x, y, z):
#     result = x if x < y else y
#     result = result if result < z else z
#     return result
# # end def
#
#
# x = 12
# y = 8
# z = 20
# result = min(x, y, z)
# print("최소 : %d" % result)
#
# result = max(x, y, z)
# print("최대 : %d" % result)