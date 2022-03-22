# python program to print the sum of squares of n natural numbers.

n = int(input("Enter a random number: "))

sum = 0

for i in range (n+1) :
    sum += i*i
    print(sum)
    
    