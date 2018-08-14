#selection sort
def printList(A, n):
    for i in range(0, n):
        print(A[i], end = ' ')
        
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def selectionSort(A, n):
    for start in range(n):
        minVal = A[start]
        for k in range(start, n):
            if A[k] < minVal:
                minVal = A[k]
                minPos = k
                swap(A, start, minPos)
        print("Pass", start+1, ": ", end = '\t')
        printList(A, n)
        print()

def main():
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)

    print("Original list:")
    printList(A, n)
    print("\n")

    print("Selection sort:")
    selectionSort(A, n)
    print()

    print("Sorted list:")
    printList(A, n)
main()
