def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

	return arr


def insertionsort(array):
	for i in range(len(array)):
		target = array[i]
		j = i

		while j > 0 and target < array[j-1]:
			array = swap(array, j, j-1)
			j -= 1

		array[j] = target

	return array
	

def main():
	arr = [10, 98, 71, 13, 76, 34, 51, 1, 0, 69, 22, 90]
	sorted_arr = insertionsort(arr)
	print(sorted_arr)

main()
