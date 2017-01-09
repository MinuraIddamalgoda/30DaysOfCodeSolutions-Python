n = int(input().strip())
strOutput = ""

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(len(arr) - 1, -1, -1):
    strOutput += str(arr[i]) + " "

print(strOutput)