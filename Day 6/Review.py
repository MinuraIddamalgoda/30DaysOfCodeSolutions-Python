n = int(input())
arrInput = []
strInput = ""
strOutput = ""

for i in range(0, n):
    arrInput.append(input())

for j in range(0, len(arrInput)):
    strInput = arrInput[j]


    strOutput = ""
    for k in range(0, len(strInput), 2):
        strOutput += strInput[k]

    print(strOutput, end="")
    print(" ", end="")

    strOutput = ""
    for l in range(1, len(strInput), 2):
        strOutput += strInput[l]

    print(strOutput, end="")
    print("")
