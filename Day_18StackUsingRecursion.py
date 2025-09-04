def sor_insert(stack, element):
    # Insert element into the sorted stack
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        sor_insert(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if stack:
        # Remove the top element
        temp = stack.pop()
        # Sort the remaining stack
        sort_stack(stack)
        # Insert the removed element in sorted order
        sor_insert(stack, temp)
    return stack
stack = [3, 1, 4, 2]
sorted_stack = sort_stack(stack)
print(sorted_stack) 
