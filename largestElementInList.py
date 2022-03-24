# python program to print the largest element in the given list.
numbers = [1, 23, 45, 7, 89, 9, 100, 98, 23, 56, 78]
largest = 0

for i in range(len(numbers)) :
    if largest < numbers[i] :
        largest = numbers[i]
        
print("The largest element in the given list : {} : is : {}".format(numbers, largest))