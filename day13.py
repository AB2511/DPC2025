def longest_palindrome(s):
    if len(s) < 2:
        return s

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    ans = s[0]
    for i in range(len(s)):
        tmp = expand(i, i)
        if len(tmp) > len(ans):
            ans = tmp

        tmp = expand(i, i+1)
        if len(tmp) > len(ans):
            ans = tmp

    return ans

print(longest_palindrome("babad"))  # "bab" 
print(longest_palindrome("cbbd"))   # "bb"
print(longest_palindrome("a"))      # "a"
print(longest_palindrome("aaaa"))   # "aaaa"
print(longest_palindrome("abc"))    # "a"
