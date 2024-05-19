class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in expression.split():
        if token.isdigit():  # Check if token is a number
            stack.push(float(token))
        elif token in operators:
            if len(stack.items) < 2:
                raise ValueError("Invalid expression")
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](operand1, operand2)
                stack.push(result)
        else:
            raise ValueError("Invalid token: " + token)

    if len(stack.items) == 1:
        return stack.pop()
    else:
        raise ValueError("Invalid expression")


def main():
    expression = input("Enter a postfix expression: ")
    try:
        result = evaluate_postfix(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
