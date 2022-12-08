fileIn = open("text.txt", "r")
print("Current text.txt text: ", fileIn.read())

fileOut = open("text.txt", "a")
fileOut.write(input("Enter whatever you want to add to the file: "))

