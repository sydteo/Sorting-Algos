def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i
        while j>0 and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

if __name__ == "__main__":
    arr = [1,6,4,3]
    n = len(arr)
    print("Before: ")
    print(arr)
    insertion_sort(arr, n)
    print("After: ")
    print(arr)

    