# python program to print the N largest numbers given in a list.
numbers_list = [1, 23, 5, 67, 9, 90, 91, 87, 23]
print("The original numbers list before sorting : {}".format(numbers_list))
largest = numbers_list[0]

# sort the list of numbers.
numbers_list_sorted = numbers_list
temp = 0
for i in range (len(numbers_list_sorted)) :
    for j in range (len(numbers_list_sorted)) :
        if numbers_list_sorted[j] > numbers_list_sorted[i] :
            temp = numbers_list_sorted[j]
            numbers_list_sorted[j] = numbers_list_sorted[i]
            numbers_list_sorted[i] = temp
            
print("The new numbers list after sorting : {}".format(numbers_list_sorted))

n = int(input("Enter the number of maximum numbers you want from the list: "))
    
# Adding the n largest numbers to the new list.
n_numbers_list = []
for i in range (n) :
    for j in range (len(numbers_list_sorted)) :
        n_numbers_list.append(numbers_list_sorted[j])
        
print(n_numbers_list)