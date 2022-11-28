def sliding_window(arr, k):
    max_sum = arr[:k]
    for i in range(1, len(arr)-k):
        sum__ = arr[i:k+i]
        if sum(sum__) > sum(max_sum):
            max_sum = sum__
    return max_sum


