def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:  # if closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[ch] != top_element:
                return False
        else:
            stack.append(ch) 
    return not stack
print(isValid("[{()}]"))   # True
print(isValid("[(])"))     # False
print(isValid("{[()]}"))   # True
print(isValid("{{{"))      # False

#opening bracket has a matching closing bracket.

#Brackets closed in the correct order.

# No unmatched or extra brackets remain.