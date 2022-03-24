# python program to remove the ith character from a given string.
# take user defined input string
string = input("Enter a random string: ") 
# calculate the length of the string
length = len(string)
print("The length of the given string is : {}".format(length))
# take the ith address to remove a particular index value from a given string.
ith = int(input("Enter a random number: "))
# holds the new string after removing the ith value
new_string = ""

# only if ith value is in bounds
if ith <= length : 
    # using the replace function to replace the character at the ith position an empty character
    new_string = string.replace(string[ith-1], "")
    
# printing the new string after removing the ith element from the string
print(new_string)