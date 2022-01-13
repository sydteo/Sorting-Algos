def quicksort(arr, left, right):
    if left<right:
        partition_pos = partition(arr, left, right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr, partition_pos+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>pivot:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i]>pivot:
        
        

if __name__ == "__main__":
    arr = [1, 9, 5, 2, -5]
    quicksort(arr, 0, len(arr)-1)
    print(arr)