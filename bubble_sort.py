def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        swap = False
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            return arr
    return arr

arr = [4,5,2,5,6,3,1]
print(arr)
print(bubble_sort(arr))