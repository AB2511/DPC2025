def find_zero_sum_subarrays(arr):
    res = []
    seen = {0: [-1]}   # prefix sum value -> indices where it showed up
    s = 0

    for i, val in enumerate(arr):
        s += val

        if s in seen:
            for j in seen[s]:
                res.append((j + 1, i))   # subarray (j+1 ... i)

        if s not in seen:
            seen[s] = []
        seen[s].append(i)

    return res
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))

print(find_zero_sum_subarrays([1, 2, 3, 4]))

print(find_zero_sum_subarrays([0, 0, 0]))

print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))

print(find_zero_sum_subarrays([1, -1, 2, -2, 3, -3] * 10**4))
