# python program to check if a given number is an armstrong number.
from operator import le
from tempfile import tempdir


number = int(input("Enter a random number: "))

tempNumber = number
number_length = len(str(number))

remainder = 0
armstrongNumber = 0

while tempNumber > 0 :
    remainder = tempNumber % 10
    armstrongNumber += remainder ** number_length
    tempNumber //= 10

print(armstrongNumber)