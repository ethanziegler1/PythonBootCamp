list1 = [3, 6, 9, 12, 15, 18]
resList = []


def FirstAndLast(listInput, listOutput):
    listOutput = [listInput[0], listInput[len(listInput)-1]]
    print(listOutput)


FirstAndLast(list1, resList)
