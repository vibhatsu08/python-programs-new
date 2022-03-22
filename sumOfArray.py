# python program to print the sum of the elements of an array.

import array as arr

array1 = arr.array("i", [1, 2, 3, 4, 5])

sum = 0

for i in range (len(array1)) :
    sum += array1[i]
    
print(sum)