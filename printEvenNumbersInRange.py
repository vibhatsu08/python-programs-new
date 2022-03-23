# python program to print all the even numbers in a given range.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end :
    start, end = end, start
    

for i in range (start, end+1) :
    if i%2 == 0:
        print(i)