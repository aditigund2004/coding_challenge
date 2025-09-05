def in_at_bottom(stack, item):
    # Helper to insert an ele at the bottom of the stack
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        in_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        # Remove the top ele
        temp = stack.pop()
        # Reverse the remaining stack
        reverse_stack(stack)
        # Insert the popped ele at the bottom
        in_at_bottom(stack, temp)
    return stack
stack = [1, 2, 3, 4]
print(reverse_stack(stack)) 
