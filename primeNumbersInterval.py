#python program to print all the prime numbers in a given interval.
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
flag = False

i=0
j=0

for i in range (start, end+1) :
    for j in range (2, end+1) :
        if i%j != 0:
            flag = True
        
if flag :
    print(i)