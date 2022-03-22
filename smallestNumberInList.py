# python program to find the smallest number in a given list.
list = [1, 23, 45, 7, 89, 9, 100, 98, 23, 56, 78]
smallest = list[0]

for i in range(len(list)) :
    if smallest > list[i] :
        smallest = list[i]
        
print("The smallest number in the given list: {} : is : {}".format(list, smallest))