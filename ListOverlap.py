list1 = [1,3,4,5,9]
list2 = [1,3,4,5,9]
resList = [number for number in list1 if list1[number-1] == list2[number-1]]
print(resList)