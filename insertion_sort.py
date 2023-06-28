def insertion_sort(arr):

    for index in range(1,len(arr)):

        key  = arr[index]
        j = index-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [2,4,6,2,3,1,5,8]
print(arr)
print(insertion_sort(arr))