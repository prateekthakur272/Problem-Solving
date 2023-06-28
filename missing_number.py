
n = int(input())
arr = []

for i in range(n-1):
    arr.append(int(input()))

current = min(arr)
for i in range(n):
    if current not in arr:
        print(current)
        break
    current = current + 1