def findLeaders(arr):
    n = len(arr)
    # list to store leaders
    leaders = []

    # the last element is always a leader
    current_max = arr[-1]
    leaders.append(current_max)

    # go from right to left
    for i in range(n - 2, -1, -1):
        # if current element is greater than everything seen so far
        if arr[i] >= current_max:
            leaders.append(arr[i])
            current_max = arr[i]

    # since we collected from right side, reverse to keep original order
    leaders = leaders[::-1]
    return leaders


# quick tests
print(findLeaders([16, 17, 4, 3, 5, 2]))    
print(findLeaders([1, 2, 3, 4, 0]))         
print(findLeaders([7, 10, 4, 10, 6, 5, 2])) 
print(findLeaders([5]))                     
print(findLeaders([100, 50, 20, 10]))   
