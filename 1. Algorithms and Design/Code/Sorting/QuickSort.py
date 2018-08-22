def QuickSort(array):
	if len(array) <= 1:				# array is sorted (0 or 1 element)
		return array

	else:
		mid = len(arr) // 2
		pivot = array.pop(mid)		# can be any valid value
		lower, higher = [], []

		for element in array:		# partition into lower and higher arrays
			if element < pivot:
				lower.append(item)

			else:
				higher.append(item)

		# calls recurive function
		return QuickSort(lower) + [pivot] + QuickSort(higher)


def main():
	arr = [10, 98, 71, 13, 76, 34, 51, 1, 0, 69, 22, 90]
	sorted_arr = QuickSort(arr)
	print(sorted_arr)

main()
