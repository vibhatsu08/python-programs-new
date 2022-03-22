# python program to check if a given number is a fibonacci number or not.
n = int(input("Enter a random number: "))

n1 = 0
n2 = 1
nextNum = 0

flag = False

for i in range (n) :
    print(nextNum)
    nextNum = n1 + n2
    n1 = n2
    n2 = nextNum

    if nextNum == n :
        flag = True
        
if flag :
    print("{} is a fibonacci number. ".format(n))
else :
    print("{} is not a fibonacci number. ".format(n))