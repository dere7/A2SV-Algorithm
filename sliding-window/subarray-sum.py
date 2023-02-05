def subarray_sum(l, k):
    n = len(l)
    res = []
    for i in range(n - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum += l[j]
        res.append(sum)
    return res

l = [1, 4, 7, 3, 2, 4, 1, 0]
print(subarray_sum(l, 3))