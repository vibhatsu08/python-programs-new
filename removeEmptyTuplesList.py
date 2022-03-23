# python program to remove empty tuples from a given list.
lst = ["apple", "banana", "orange", 1234, True, False, (), "helloworld"]
print(lst)

for i in lst :
    if i == () :
        lst.remove(i)
        
print(lst)