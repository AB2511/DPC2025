def sort_stack(stack):
    if len(stack) <= 1:
        return
    # take out the top element
    top = stack.pop()
    # sort the rest of the stack
    sort_stack(stack)
    # put the top element back in the right place
    insert_in_order(stack, top)
def insert_in_order(stack, value):
    
    if not stack or stack[-1] <= value:
        stack.append(value)
        return
   
    top = stack.pop()
    insert_in_order(stack, value)
    stack.append(top)
stack1 = [3, 1, 4, 2]
sort_stack(stack1)
print(stack1)  # [1, 2, 3, 4]

stack2 = [7, 1, 5]
sort_stack(stack2)
print(stack2)  # [1, 5, 7]

stack3 = [5]
sort_stack(stack3)
print(stack3)  # [5]

stack4 = [-3, 14, 8, 2]
sort_stack(stack4)
print(stack4)  # [-3, 2, 8, 14]

stack5 = []
sort_stack(stack5)
print(stack5)  # []

stack6 = [3, 3, 3]
sort_stack(stack6)
print(stack6)  # [3, 3, 3]

