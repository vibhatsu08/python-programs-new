# python program to print the max of three numbers with functions in python
num1 = int(input("Enter a random number: "))
num2 = int(input("Enter a random number: "))
num3 = int(input("Enter a random number: "))
def printMax (num1, num2, num3) :
    maxNum = 0
    if num1 >= num2 and num1 >= num3 :
        maxNum = num1
        print("The largest number among the three numbers : {} {} {} is {}".format(num1, num2, num3, maxNum))
    elif num2 >= num1 and num2 >= num3 :
        maxNum = num2
        print("The largest number among the three numbers : {} {} {} is {}".format(num1, num2, num3, maxNum))
        
    elif num3 >= num1 and num3 >= num2 :
        maxNum = num2
        print("The largest number among the three numbers : {} {} {} is {}".format(num1, num2, num3, maxNum))
        
printMax(num1, num2, num3)