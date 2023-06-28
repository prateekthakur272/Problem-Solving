def is_heap(arr,i):
    n = len(arr)-1
    if i >= (n-1)//2:
        return True
    return (arr[i]>=arr[2*i+1] and arr[i]>=arr[2*i+2] and is_heap(arr, 2*i+1) and is_heap(arr, 2*i+2))

arr = [90, 15, 10, 7, 12, 2, 7, 3]
print(is_heap(arr,0))