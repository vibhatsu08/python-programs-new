#python program to print the fibonacci sequence upto a number.
number = int(input("Enter a random number: "))

num1 = 0
num2 = 1
nextNumber=0

count = 0

while count < number :
    print(num1)
    nextNumber = num1 + num2
    num1 = num2
    num2 = nextNumber
    count += 1
    

    