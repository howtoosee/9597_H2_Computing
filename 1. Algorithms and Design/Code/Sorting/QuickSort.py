def QuickSort(array):
	if len(array) <= 1:
		return array

	else:
		pivot = array.pop(0)		# can be any valid value
		less = []
		greater = []

		for item in array:
			if item < pivot:
				less.append(item)
			else:
				greater.append(item)

	return QuickSort(less) + [pivot] + QuickSort(greater)


def main():
	arr = [10, 98, 71, 13, 76, 34, 51, 1, 0, 69, 22, 90]
	sorted_arr = QuickSort(arr)
	print(sorted_arr)

main()
