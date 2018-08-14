#CheckDigit

def checkDigit():
    ic = []
    nricDigit = ["A", "B", "C", "D","E", "F", "G", "H", "I", "Z", "J"]
    finDigit = ["K", "L", "M", "N", "P", "Q", "R", "T", "U", "W", "X"]

    NRIC = input("Enter NRIC or FIN without last letter: ")
    for char in NRIC:
        ic.append(char.upper())

    total = 0
       
    if ic[0] == 'T' or ic[0] == 'G':
        total = 4
        
    total += int(ic[1]) * 2
    m = 7

    for i in range(2,8):
        total += int(ic[i]) * m
        m -= 1
    digitId = 11 - (total % 11)

    if ic[0] == 'T' or ic[0] == 'S':
        digit = nricDigit[digitId - 1]

    elif ic[0] == "F" or ic[0] == "G":
        digit = finDigit[digitId - 1]

    print("The check digit is:", digit)
    print("The full IC number is: ", NRIC.upper(), digit, sep='')

checkDigit()
