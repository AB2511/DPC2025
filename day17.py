def prime_factors(n):
    result = []

    while n % 2 == 0:
        result.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 2  

    if n > 1:
        result.append(n)

    return result

print(prime_factors(30))       # [2, 3, 5]
print(prime_factors(49))       # [7, 7]
print(prime_factors(19))       # [19]
print(prime_factors(64))       # [2, 2, 2, 2, 2, 2]
print(prime_factors(123456))   # [2, 2, 2, 2, 2, 3, 643]
