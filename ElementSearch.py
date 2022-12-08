list1 = [1, 3, 5, 4, 2, 6, 5, 3, 7, 4, 8, 5, 4, 3]

uInput = int(input("What letter would you like to check if is in list? \n"))
countOfNum = list1.count(uInput)
if countOfNum > 0:
    print("Your value is in the list. There are ", countOfNum, " instances of your number in the list")
else:
    print("Your value is not in the list")
