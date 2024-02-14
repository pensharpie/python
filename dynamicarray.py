'''
2/13/2023, Herbe Chun
Script demonstrates the concept of dyanmic arrays.  Dynamic arrays are arrays
which increases its capacity when its length is equal to its capacity.
'''
import numpy as np

TWO = 2

class array1():
    def __init__(self, arr, length, capacity):
        self.arr = arr
        self.length = length
        self.capacity = capacity

    def conc(self, i):
        if i < self.length:
            return self.arr[i]
        if i >= self.length:
            return self.arr[i - self.length]

class array2():
    def __init__(self, arr, length, capacity):
        self.arr = arr
        self.length = length
        self.capacity = capacity

    def assign(self, i, arr, length):
        self.length = length
        if (self.length < self.capacity):
            self.arr[i] = arr
            print("self.arr[i] =", self.arr[i], ", index =", i, ", arr[i] =", arr, ", length =", length, " capacity =", self.capacity)
        if (self.length == self.capacity):
            self.capacity = 2 * self.capacity
            self.arr = np.array(self.arr)
            self.arr = np.resize(self.arr, (self.capacity))
            self.arr[i] = arr
            print("self.arr[i] =", self.arr[i], ", index =", i, ", arr[i] =", arr, ", length =", length, " capacity =", self.capacity)
        
def main():
    length = 3
    capacity = length 
    arr1 = ["1","2","1"]
    arr2 = ["0","0","0"]
    
    c1 = array1(arr1, length, capacity)
    c2 = array2(arr2, length, capacity)
    print("Array1 =", arr1, ", length =", length, ", capacity =", capacity)
    print("Array2 =", arr2, ", length =", length, ", capacity =", capacity)
    
    for i in range(2 * length):
        c2.assign(i, c1.conc(i), i + 1)
        
    
if __name__ == "__main__":
    main()