import time
import matplotlib.pyplot as plt
import numpy as np

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("")

def insertionSort(arr):
    global count1
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0:
            count1+=1
            if(arr[j] > key):
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

def mergeSort(arr):
    global count
    if len(arr) > 1:
        mid = len(arr)//2
        
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
    
        while i < len(L) and j < len(R):
            count +=1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# if array size is smaller than threshold, do insertionSort, else mergeSort
def mergesertionSort(arr):
    if len(arr) > 10:
        mergeSort(arr)
    else:
        insertionSort(arr)



import numpy as np
import time

count = 0
np.random.seed(42)
arr = np.random.rand(1000000)
start_time = time.time()
mergeSort(arr)
counter = count
end_time = (time.time() - start_time)
print("CPU Time:", end_time)
print("Comparisons:", counter)