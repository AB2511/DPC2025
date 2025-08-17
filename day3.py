def findDuplicate(arr):
    # detect cycle
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # find entry point
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


# valid test cases
print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 7, 1, 4]))  
print(findDuplicate([4, 3, 6, 2, 1, 6, 5]))         
print(findDuplicate([7, 2, 4, 5, 3, 1, 7, 6]))       
print(findDuplicate([1, 3, 4, 5, 2, 3]))             
print(findDuplicate([2, 2, 2, 2, 2]))                
