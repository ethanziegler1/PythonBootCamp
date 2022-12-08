listOfNums = []
for i in range(10):
    listOfNums.append(int(input("Enter a number to be in index of the array")))
sum = 0
for i in range(len(listOfNums)):
    sum = sum + listOfNums[i]

if sum <= 10:
    print("Your list's sum is less than 10. Value of list: ", sum)
else:
    print("Your list's sum is more than 10. Value of list: ", sum)
