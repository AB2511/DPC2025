def count_substrings_with_k_distinct(s, k):

    def at_most(k):
        left = 0
        seen = {}
        count = 0

        for right in range(len(s)):
            ch = s[right]
            seen[ch] = seen.get(ch, 0) + 1

            while len(seen) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1

            count += (right - left + 1)

        return count

    if k <= 0:
        return 0
    return at_most(k) - at_most(k - 1)

print(count_substrings_with_k_distinct("pqpqs", 2))        # 7
print(count_substrings_with_k_distinct("aabacbebebe", 3))  # 10
print(count_substrings_with_k_distinct("a", 1))            # 1
print(count_substrings_with_k_distinct("abc", 3))          # 1
print(count_substrings_with_k_distinct("abc", 2))          # 2
