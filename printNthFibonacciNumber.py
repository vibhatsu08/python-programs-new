# python program to print the nth fibonacci number of the series.

n = int(input("Enter a random number: "))

n1 = 0
n2 = 1
nextNum = 0

for i in range (n) :
    print(nextNum)
    nextNum = n1 + n2
    n2 = n1
    n1 = nextNum
    
    