# python program to print the largest element of a given array.

import array as array

array1 = array.array("i", [1, 23, 2, 89, 23, 21, 90, 23])
print(array1)

largestElement = array1[0]

for i in range (len(array1)) :
    for j in range (i+1, len(array1)) :
        if largestElement < array1[i] :
            largestElement = array1[i]
            
print(largestElement)