#python program to interchange the first and the last elements of a list.
fruits = ["apple", "banana", "grapes", "orange", "mango"]
print(fruits)
fruits.replace(fruits[0], fruits[len(fruits)-1])
print(fruits)