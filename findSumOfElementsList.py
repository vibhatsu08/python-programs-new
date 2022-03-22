# python program to find the sum of elements/numbers in a given list.
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for i in numbers_list :
    sum += i
    
print("The sum of the given numbers in the list: {} : is : {}".format(numbers_list, sum))