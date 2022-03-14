#python program to check if a given number is a prime number or not.
number = int(input("Enter a random number: "))

flag = True #for prime number
for i in range(2, number):
    if (number%i) == 0:
        flag = False
        break

if flag:
    print("prime number")
else:
    print("not prime number")