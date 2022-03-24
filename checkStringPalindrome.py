# python program to check if a given string is a palindrome or not.
string = input("Enter a random string: ")
new_string = ""

for i in string :
    new_string = i + new_string
    
if new_string == string :
    print("{} is palindrome.".format(new_string))
else :
    print("{} is not palindrome.".format(new_string))
    