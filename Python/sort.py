def bubble(arr):
    n = len(arr)
    for x in range(n):
        for y in range(n-1-x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr

print(bubble([4,3,5,6,7,0,9,1]))