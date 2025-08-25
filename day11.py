def permute_unique(s):
    if not s:
        return ['']

    chars = sorted(s)
    used = [False] * len(chars)
    path = []
    out = []

    def dfs():
        if len(path) == len(chars):
            out.append(''.join(path))
            return
        for i, ch in enumerate(chars):
            if used[i]:
                continue
            if i > 0 and ch == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(ch)
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return out

if __name__ == "__main__":
    print(sorted(permute_unique("abc")))   # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(sorted(permute_unique("aab")))   # ['aab', 'aba', 'baa']
    print(sorted(permute_unique("aaa")))   # ['aaa']
    print(permute_unique("a"))             # ['a']
    print(len(permute_unique("abcd")))     # 24
