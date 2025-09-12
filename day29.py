def fib(n):
    if n < 2:
        return n

    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

print(fib(0))   # 0
print(fib(1))   # 1
print(fib(5))   # 5
print(fib(10))  # 55

# large n
print(fib(50))    # 12586269025
print(fib(100))   # 354224848179261915075
