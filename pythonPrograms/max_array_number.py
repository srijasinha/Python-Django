# maximum of number in an array
def max_arr(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [2, 3, 41, 61]
n = len(arr)
print(max_arr(arr, n))
