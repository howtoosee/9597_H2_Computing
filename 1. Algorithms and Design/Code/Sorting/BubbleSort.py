def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

	return arr


def bubblesort(array):
	n = len(array)

	isSorted = False
	while not isSorted and n > 0:
		isSorted = True

		for i in range(n-1):
			if array[i] > array[i + 1]:
				array = swap(array, i, i+1)
				isSorted = False
		n -= 1

	return array


def main():
	arr = [10, 98, 71, 13, 76, 34, 51, 1, 0, 69, 22, 90]
	sorted_arr = bubblesort(arr)
	print(sorted_arr)

main()
