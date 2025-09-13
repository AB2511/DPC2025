def coin_change(coins, amount):
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  

    for c in coins:
        for i in range(c, amount + 1):
            if dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    return -1 if dp[amount] == float('inf') else dp[amount]

print(coin_change([1, 2, 5], 11))   # 3 
print(coin_change([2], 3))          # -1
print(coin_change([1], 0))          # 0
print(coin_change([2, 4], 7))       # -1
print(coin_change([1, 3, 4], 6))    # 2 
