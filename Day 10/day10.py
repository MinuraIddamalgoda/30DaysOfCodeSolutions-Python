n = int(input())
remainderArr = []

while(n>0):
    remainder = n%2
    n = n/2
    remainderArr.append(remainder)

print remainderArr