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

def infixToPostfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    stack = Stack()
    postfix = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isdigit():  # Operand
            postfix.append(token)
        elif token == '(':  # Left parenthesis
            stack.push(token)
        elif token == ')':  # Right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)

def main():
    #expression = input("Enter an infix expression: ")
    # some tests
    expression = '2 * (1 + 3)'
    print(f'Infix expression {expression}')
    try:
        postfix = infixToPostfix(expression)
        print("Postfix expression:", postfix)
    except Exception as e:
        print("Error:", e)
        
    expression = '2 * (1 + 3)'
    print(f'Infix expression {expression}')
    try:
        postfix = infixToPostfix(expression)
        print("Postfix expression:", postfix)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
