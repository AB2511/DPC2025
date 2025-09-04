def reverse_stack(stack):
    if not stack:
        return
    
    top = stack.pop()
    reverse_stack(stack)
    _push_to_bottom(stack, top)

def _push_to_bottom(stack, x):
    if not stack:
        stack.append(x)
        return
    temp = stack.pop()
    _push_to_bottom(stack, x)
    stack.append(temp)

data = [1, 2, 3, 4]
reverse_stack(data)
print(data)  # [4, 3, 2, 1]

single = [5]
reverse_stack(single)
print(single)  # [5]

empty = []
reverse_stack(empty)
print(empty)  # []

neg = [-5, -10, -15]
reverse_stack(neg)
print(neg)  # [-15, -10, -5]
