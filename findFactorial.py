#python program to find the factorial of a given number
from math import factorial


number = int(input("Enter a random number: "))
factorial = 1

for i in range(1, number+1):
    factorial *= i

print(factorial)