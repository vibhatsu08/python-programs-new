# python program to multiply the numbers in a given list.
from math import prod


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = 1

for i in numbers_list :
    product *= i
    
print("The product of the numbers in the given list: {} : is : {}".format(numbers_list, product))