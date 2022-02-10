def mergesort(arr,counter):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        mergesort(left_arr,counter)
        mergesort(right_arr,counter)

        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            counter += 1
            k+=1

        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    return arr,counter

print(mergesort([4,3,90],1))

