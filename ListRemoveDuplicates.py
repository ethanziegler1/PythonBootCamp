list1 = [1,2,3,4,5,2,7,8,3]
for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)
    else:
        continue
print(list1)