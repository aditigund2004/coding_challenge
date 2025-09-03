def eval_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():   # check if operand (handles negatives too)
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # integer division, truncate toward 0
                stack.append(int(a / b))
    return stack[0]
expr = "2 1 + 3 *"
print(eval_postfix(expr)) 
