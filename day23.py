from collections import deque

def sliding_window_max(arr, k):
    if k <= 0 or not arr:
        return []

    q = deque()  
    out = []

    for i, val in enumerate(arr):
        if q and q[0] <= i - k:
            q.popleft()

        while q and arr[q[-1]] < val:
            q.pop()

        q.append(i)

        if i >= k - 1:
            out.append(arr[q[0]])

    return out

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
print(sliding_window_max([1, 5, 3, 2, 4, 6], 3))           # [5, 5, 4, 6]
print(sliding_window_max([1, 2, 3, 4], 2))                 # [2, 3, 4]
print(sliding_window_max([7, 7, 7, 7], 1))                 # [7, 7, 7, 7]
print(sliding_window_max([10], 1))                         # [10]
