def reverse_words(s):
    # split on spaces 
    parts = s.split()
    # reverse using slicing
    return " ".join(parts[::-1])

print(reverse_words("the sky is blue"))        # blue is sky the
print(reverse_words("  hello world  "))        # world hello
print(reverse_words("a good   example"))       # example good a
print(reverse_words("    "))                   # ""
print(reverse_words("word"))                   # word
