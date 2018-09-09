#find all prime numbers from 0 - num

from math import sqrt
num = int(input("enter number: "))
set = [True for i in range(num+1)]

def method1(num):
    for m in range(2, int(sqrt(num)+1)):
        if set[m] == True:
            for n in range(m*m, num+1, m):
                set[n] = False


def method2(num):
    p = 2
    while (p*p <= num):
        if set[p] == True:
            for i in range(p*p, num+1, p):
                set[i] = False
        p += 1

print("Primes: ", end = "")
for i in range(2, num+1):
    if set[i] == True:
        print(i, end = " ")
print()

method1(num)
method2(num)
