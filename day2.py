def find_missing_number(arr):
    # length of array is n-1, so missing sequence length is n
    n = len(arr) + 1  
    
    # expected sum of first n natural numbers
    expected = (n * (n + 1)) // 2  
    
    # actual sum from given array
    actual = 0
    for num in arr:
        actual += num
    
    # the gap is the missing number
    missing = expected - actual
    return missing


# quick tests
print(find_missing_number([1, 2, 4, 5]))   
print(find_missing_number([2, 3, 4, 5]))   
print(find_missing_number([1, 2, 3, 4]))   
print(find_missing_number([1]))            
print(find_missing_number(list(range(1, 1000000))))  
