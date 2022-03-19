#python program to reverse a given number
number = int(input("Enter a random number: "))
tempNumber = number

reverseNumber = 0

while tempNumber != 0:
    remainder = tempNumber % 10
    reverseNumber = reverseNumber * 10 + remainder
    tempNumber /= 10

print(number)
print(reverseNumber)
