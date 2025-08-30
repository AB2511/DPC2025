def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n, m):
    g = gcd(n, m)
    return (n * m) // g

print(lcm(4, 6))          # 12
print(lcm(5, 10))         # 10
print(lcm(7, 3))          # 21
print(lcm(1, 987654321))  # 987654321
print(lcm(123456, 789012))# 8117355456
