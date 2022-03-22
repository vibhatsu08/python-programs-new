# python program to check if an element is present in a list or not.
# method 1
fruits = ["apple", "banana", "orange", "mango"]
check_fruit = input("Enter a random fruit: ")

if check_fruit in fruits :
    print("{} is in the given list: {}".format(check_fruit, fruits))
    
