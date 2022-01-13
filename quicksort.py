def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1
    while i < j:
        while i < right and arr[i] < pivot:
            i+=1
        while j > left and arr[j] >= pivot:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


if __name__ == "__main__":
    arr = [5, 4, 8, 7, 1]
    quicksort(arr,0,len(arr)-1)
    print(arr)