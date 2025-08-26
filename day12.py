def is_valid(s: str) -> bool:
    if len(s) % 2:  
        return False

    match = {')': '(', ']': '[', '}': '{'}
    stack = []

    for c in s:
        if c in match.values():
            stack.append(c)
        elif c in match:
            if not stack or stack[-1] != match[c]:
                return False
            stack.pop()
        else:
            return False
    return not stack

print(is_valid("()"))        # True
print(is_valid("([)]"))      # False
print(is_valid("[{()}]"))    # True
print(is_valid(""))          # True
print(is_valid("{[}"))       # False
print(is_valid("["))         # False
print(is_valid("]"))         # False
print(is_valid("((("))       # False
print(is_valid("()[]{}"))    # True
