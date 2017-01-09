import sys

n = int(input().strip())

for i in range(1, 11, 1):
    multiple = n * i
    print(str(n) + ' X ' + str(i) + ' = ' + str(multiple))
