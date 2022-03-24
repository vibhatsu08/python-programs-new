# python program to interchange the first and the last elements of a list.
# method 1
# fruits = ["apple", "banana", "grapes", "orange", "mango"]
# print(fruits)
# fruits.replace(fruits[0], fruits[len(fruits)-1])
# print(fruits)

# method 2
fruits = ["apple", "banana", "grapes", "orange", "mango"]
print(fruits)
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)
