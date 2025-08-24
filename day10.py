from collections import defaultdict

def group_anagrams_sorted(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))   # sorted letters => same key for anagrams
        groups[key].append(s)
    return list(groups.values())


# Tests (direct prints, expected outputs commented)
print(group_anagrams_sorted(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]

print(group_anagrams_sorted([""]))
# [[""]]

print(group_anagrams_sorted(["a"]))
# [["a"]]

print(group_anagrams_sorted(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))
# [["abc","bca","cab"], ["xyz","zyx","yxz"]]

print(group_anagrams_sorted(["abc", "def", "ghi"]))
# [["abc"], ["def"], ["ghi"]]
