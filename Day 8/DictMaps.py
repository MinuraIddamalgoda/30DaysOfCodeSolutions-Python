n = int(input())
phoneBook = dict()

for i in range(0, n):
    inputStr = input()
    dictKey = inputStr.split(' ', 1)[0]
    dictValue = inputStr.split(' ', 1)[1]
    phoneBook[dictKey] = dictValue

for j in range(0, n):
    queryStr = input()
    if queryStr in phoneBook:
        print(queryStr + "=" + phoneBook[queryStr])
    else:
        print("Not found")