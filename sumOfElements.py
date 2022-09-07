# To find sum of elements in given array

def _sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return(sum)

arr = []

arr = [11, 2, 6, 20]

n = len(arr)

ans = _sum(arr)

print('Sum of the array is ', ans)
