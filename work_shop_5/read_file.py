file = open("file1.txt", "r")
line = file.readline()
while line != '':
    print(line)
    line = file.readline()

file.close()