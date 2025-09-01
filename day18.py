def count_divisors(n: int) -> int:
    if n == 1:
        return 1  

    count = 0
    divisor = 1

    while divisor * divisor <= n:
        if n % divisor == 0:
            other = n // divisor
            if other == divisor:  
                count += 1
            else:
                count += 2 
        divisor += 1

    return count

print(count_divisors(12))   # 6
print(count_divisors(18))   # 6
print(count_divisors(29))   # 2
print(count_divisors(100))  # 9
print(count_divisors(1))    # 1
print(count_divisors(997))  # 2
print(count_divisors(36))   # 9
