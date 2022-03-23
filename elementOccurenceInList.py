# python program to find the occurrence of an element in the list.
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
element = 8
count = 0

for i in lst :
    if i == element :
        count += 1
        
print("The number of times the element : {} : was found in the list : {}: is : {}".format(element, lst, count))