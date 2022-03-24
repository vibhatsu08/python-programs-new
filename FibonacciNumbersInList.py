def checkFibonacciNumber (n) :
    n = int(input("Enter a random number: "))

    n1 = 0
    n2 = 1
    nextNum = 0

    flag = False    

    for i in range (n) :
        nextNum = n1 + n2
        n1 = n2
        n2 = nextNum

        if nextNum == n :
            flag = True
        
    if flag :
        print("{} is a fibonacci number. ".format(n))
    else :
        print("{} is not a fibonacci number. ".format(n))
        
lst = [0, 12, 3, 23, 12, 89, 34, 55]
    
for i in lst :
    
