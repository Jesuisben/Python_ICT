mylist = [10, -20, 30, -40, 50]

total = 0
for item in mylist:
    if item < 0 :
        item = abs(item)
    total += item

print(total)
print('-'*30)
for idx in range(len(mylist)):
    if mylist[idx] < 0:
        mylist[idx] = abs(mylist[idx])

print(mylist)
print(sum(mylist))
print('-'*30)