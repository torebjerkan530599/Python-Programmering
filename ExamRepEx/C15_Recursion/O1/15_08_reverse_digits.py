
class Recursives():
    
    def __init__(self) -> None:
        pass
        
    def reverse_digits(self,integer) -> int:
        if integer < 10:
            return integer
        else:
            return int(str(integer%10) + str(self.reverse_digits(integer // 10)))

def main():
    digits = int(input('Enter digits to be reversed: '))
    recursion = Recursives()
    digits = recursion.reverse_digits(digits)
    print(digits)
    
# Call the main function.
if __name__ == '__main__':
      main()
      
#alternative

def reverse(digits):
    if digits != 0:
        print(digits%10)
        value = digits // 10
        reverse(value)
reverse(12345)