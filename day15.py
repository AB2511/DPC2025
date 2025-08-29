def longest_unique_substring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    last_seen = {}
    start = 0   
    max_len = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:

            start = last_seen[ch] + 1

        last_seen[ch] = i
        window_len = i - start + 1
        if window_len > max_len:
            max_len = window_len

    return max_len

print(longest_unique_substring("abcabcbb"))  # 3 ("abc")
print(longest_unique_substring("bbbbb"))     # 1 ("b")
print(longest_unique_substring("pwwkew"))    # 3 ("wke")
print(longest_unique_substring("abcdefgh"))  # 8 ("abcdefgh")
print(longest_unique_substring("a"))         # 1 ("a")
