def eval_postfix(expr: str) -> int:
    stack = []
    for token in expr.split():
        if token.lstrip('-').isdigit():   # number (handles negatives too)
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # force truncation toward 0
            else:
                raise ValueError(f"bad operator: {token}")
    return stack[-1]
print(eval_postfix("2 1 + 3 *"))                  # 9
print(eval_postfix("5 6 +"))                      # 11
print(eval_postfix("-5 6 -"))                     # -11
print(eval_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))  # 5
print(eval_postfix("5"))                          # 5
