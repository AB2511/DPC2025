def merge(arr1, arr2):
    import math
    m, n = len(arr1), len(arr2)

    # helper for next gap
    def ng(g):
        if g <= 1: return 0
        return (g + 1) // 2   # ceil division, shorter than math.ceil

    gap = ng(m + n)
    while gap > 0:
        i, j = 0, gap
        while j < m + n:
            if j < m:   # both in arr1
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
            elif i < m:  # i in arr1, j in arr2
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
            else:        # both in arr2
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]
            i += 1
            j += 1

        gap = ng(gap)


# quick checks
a, b = [1, 3, 5], [2, 4, 6]
merge(a, b)
print(a, b)   

a, b = [10, 12, 14], [1, 3, 5]   # one arr entirely bigger
merge(a, b)
print(a, b)   

a, b = [1], [2]   # trivial case
merge(a, b)
print(a, b)

a, b = [1, 2, 3, 4], [5, 6, 7]   # already sorted, no swaps
merge(a, b)
print(a, b)

a, b = [1, 2, 3, 4, 5], [100000]  # highly uneven size
merge(a, b)
print(a, b)
