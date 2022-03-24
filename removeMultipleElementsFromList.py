# python program to remove multiple elements from a given list.
numbers_list = [1, 23, 32, 45, 7, 4, 34, 76, 87, 44, 37, 45, 23]
print(numbers_list)

for i in numbers_list :
    if i%2 == 0 :
        numbers_list.remove(i)
        
print(numbers_list)