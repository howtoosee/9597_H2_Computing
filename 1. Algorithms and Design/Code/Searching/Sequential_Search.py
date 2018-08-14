def Sequential_Search(array, target):

	for i in range(len(array)):

		if array[i] == target:
			
			return i
	

def main():
	arr = [7, 19, 33, 57, 90, 100, 195, 299]
	target = 33

	pos = Sequential_Search(arr, target)

print("Number 33 is found at array index", pos)


main()