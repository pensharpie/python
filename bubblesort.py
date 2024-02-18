'''
2/18/2024
Super simple bubble sort
'''

def swap(arr, j):
	temp = arr[j]
	arr[j] = arr[j-1]
	arr[j-1] = temp
	return arr

def main():
	num = [5,2,3,1]
	for i in range(len(num)):
		for j in range(len(num) - 1):
			if num[j+1] < num[j]:
				num = swap(num, j)
	print(num)
	
if __name__ == "__main__":
	main()