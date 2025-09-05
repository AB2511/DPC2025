def first_k_times(arr, k):
    counts = {}

    # first pass: count how many times each element shows up
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # second pass: find the first one that hit exactly k
    for num in arr:
        if counts[num] == k:
            return num

    return -1

print(first_k_times([3, 1, 4, 4, 5, 2, 6, 1, 4], 2))  # expect 1
print(first_k_times([2, 3, 4, 2, 2, 5, 5], 2))        # expect 5
print(first_k_times([1, 1, 1, 1], 1))                 # expect -1
print(first_k_times([10], 1))                         # expect 10
print(first_k_times([6, 6, 6, 6, 7, 7, 8, 8, 8], 3))  # expect 8
