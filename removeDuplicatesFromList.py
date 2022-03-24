# python program to remove duplicates from the given list of numbers.
numbers_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(numbers_list)
count = 0
i = 0
j = i + 1
for i in numbers_list :    
    for j in numbers_list :
        if j == i:
            count += 1
            if count > 1 :
                numbers_list.remove(j)
                
print(numbers_list)