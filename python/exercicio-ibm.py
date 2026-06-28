def maxTrailing(arr):
    result = -1
    menor = arr[0]
    for i in range(1, len(arr)):
        diff = arr[i] - menor
        if diff > result and diff > 0:
            result = diff
        if arr[i] < menor:
            menor = arr[i]
    return result
