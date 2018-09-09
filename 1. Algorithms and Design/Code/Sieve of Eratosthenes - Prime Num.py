#find all prime numbers from 0 - num

from math import sqrt
num = int(input("enter number: "))
set = list(range(num+1))

for i in range(2, num+1):						# assume all to be primes
    set[i] = True

for m in range(2, int(sqrt(num)+1)):			# filter out non-primes
        if set[m] == True:
            for n in range(m*m, num+1, m):		# (m*m) to increase efficiency
                set[n] = False

print("Primes: ", end = "")
    for i in range(2, num+1):
        if set[i] == True:
            print(i, end = " ")
