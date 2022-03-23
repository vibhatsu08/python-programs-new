# python program to check if a given string is a palindrome or not.
string = input("Enter a random string: ")
new_string = ""

for i in string :
    new_string = i + new_string
    
if new_string == string :
    print("Given string : {} : is palindrome.".format(string))
elif new_string != string:
    print("Given string : {} is not palindrome.".format(string))