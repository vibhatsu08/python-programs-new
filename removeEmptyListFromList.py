# python program to remove empty list from a given list.
new_list = ["apple", 12, "banana", True, [], False, "helloworld", 89]
print(new_list)

for i in new_list :
    if i == [] :
        new_list.remove(i)

print(new_list)

# creating a new list using list comprehension to print the updated list.
new_list1 = ["apple", 12, "banana", True, [], False, "helloworld", 89]
print(new_list1)

updated_list = [i for i in new_list if i != []]

print(updated_list)