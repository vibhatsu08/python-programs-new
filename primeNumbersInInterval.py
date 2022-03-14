#python program to print all prime numbers in an interval
print("Enter a starting point and an ending point: ")
start = int(input())
end = int(input())

for i in range (start, end+1):
    for j in range (2, i):
        if i%j == 0:
            break
    else:
        print(i)
