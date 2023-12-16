def infix_to_postfix(infix_expression):
    def get_precedence(operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^':3}
        return precedence.get(operator, 0)
    infix_expression = infix_expression.replace(" ", "")
    ops = []
    output = []
    
    for token in infix_expression:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()  # Pop the '('
        elif token in {'+', '-', '*', '/'}:
            while ops and get_precedence(ops[-1]) >= get_precedence(token):
                output.append(ops.pop())
            ops.append(token)

    while ops:
        output.append(ops.pop())

    return ''.join(output)

# Example usage:
infix_expression = "A+B+C"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
