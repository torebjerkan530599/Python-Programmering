from Calculator import Calculator

def main():
    calculator = Calculator()
    calculator.calculate(1,2,'+')
    calculator.calculate(2,2,'*')
    calculator.calculate(16,2,'/')
    print(calculator.get_log())
    print(calculator.get_last_logged())

main()