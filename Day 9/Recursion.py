n = int(input())

def factorial(N):
    fac_n = 1
    c = 1
    while c <= N:
        fac_n *= c
        c += 1

    return fac_n

print(str(factorial(n)))
