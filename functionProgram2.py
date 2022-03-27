# python program to print the factorial of a number using functions.
def factorial (number) :
    if number == 1:
        return 1
    else :
        return (number * factorial(number-1))
    
print(factorial(3))