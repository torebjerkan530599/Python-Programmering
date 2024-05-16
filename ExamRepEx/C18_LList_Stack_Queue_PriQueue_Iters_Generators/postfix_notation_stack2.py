class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression):
    operand_stack = Stack()

    # Extract operands and operators
    tokens = expression.split()

    # Phase 1: Scan tokens
    for token in tokens:
        token = token.strip()  # Extract a token
        if not token:  # Blank space
            continue  # Back to the loop to extract the next token
        elif token in {'+', '-', '*', '/'}:
            process_operator(token, operand_stack)
        else:  # An operand scanned
            operand_stack.push(int(token))

    # Return the result
    return str(operand_stack.pop())

def process_operator(op, operand_stack):
    op2 = operand_stack.pop()
    op1 = operand_stack.pop()
    if op == '+':
        operand_stack.push(op1 + op2)
    elif op == '-':
        operand_stack.push(op1 - op2)
    elif op == '*':
        operand_stack.push(op1 * op2)
    elif op == '/':
        operand_stack.push(op1 / op2)

# Example usage:
expression = "5 3 2 * +"
result = evaluate_expression(expression)
print("Result:", result)
