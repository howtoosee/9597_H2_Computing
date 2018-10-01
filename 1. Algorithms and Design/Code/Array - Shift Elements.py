from random import randint

def shift(arr, old_start, new_start, length):
	if new_start == old_start:
		return arr


	if old_start > new_start:
		start_index = old_start
		end_index = old_start + length
		step = 1

	else:
		start_index = old_start + length
		end_index = old_start
		step = -1

	for i in range(start_index, end_index, step):
		arr[new_start - old_start + i] = arr[i]
		arr[i] = ""

	return arr


def main():
	arr = [""]*20
	new_arr = [""]*20

	start = randint(0, 9)
	print("Original start:", start)

	for i in range(0, 10):
		num = randint(0, 100)
		arr[start+i] = str(num)

	print(arr)
	newstart = int(input("Enter new start: "))
	new_arr = shift(arr, start, newstart, 10)

	print(new_arr)


main()
