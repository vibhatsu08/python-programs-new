# python program to print the sum of digits given in a list.
lst = [12, 67, 98, 34]
sum = 0

for i in lst :
    sum += i
    
print("The sum of numbers in the given list: {} : is : {}".format(lst, sum))