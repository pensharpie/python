'''
2/19/2024
A simple binary search using recursion
Herbe Chun
'''

def bsearch(arr, target, indexStart, indexEnd, count):
	indexMid = int((indexStart + indexEnd) / 2)
	if count < 10:
		print(indexMid, indexStart, indexEnd)
	if (arr[indexMid] == target):
		print("index =", indexMid)
		return 
	elif (arr[indexMid] > target):
		indexStart = 0
		indexEnd = indexMid - 1
	elif (arr[indexMid] < target):
		indexStart = indexMid + 1
		indexEnd = indexEnd
	count += 1
	bsearch(arr, target, indexStart, indexEnd, count)
	
def main():
	nums = [-1, 0, 3, 5, 9, 12, 15, 20, 24, 25, 51]
	target = 9
	indexStart = 0
	indexEnd = len(nums) - 1
	count = 0
		
	bsearch (nums, target, indexStart, indexEnd, count)
	
if __name__  == "__main__":
	main()