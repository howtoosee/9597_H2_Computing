# direct access file


# create test file
test = open("test.txt", 'w')
for i in range(1, 5+1):
    test.write(str(i) * 5 + '\r\n')
test.close()


# read 3 lines and return pointer position
test = open("test.txt", 'r')
for i in range(3):
    print(test.readline().strip())
position = test.tell()
print("Position: {} bytes.".format(position))

# go to the beginning
test.seek(0)
print(test.readline().strip())
length = test.tell()
print("Line length: {} bytes.".format(length))
