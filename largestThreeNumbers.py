#python program to check for the largest number among three numbers
print("Enter three random numbers: ")
number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 >= number2 and number1 >= number3:
    print(str(number1) + " is the largest number.")
elif number2 >= number1 and number2 >= number3:
    print(str(number2) + " is the largest number.")
elif number3 >= number1 and number3 >= number2:
    print(str(number3) + " is the largest number.")


