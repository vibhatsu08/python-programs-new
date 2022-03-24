# python program to check if a given string is palindrome or symmetrical
string = input("Enter a random string : ")
# to calculate the length of the given string
length = len(string)
# find out the half of the string
half = (length)//2

# first half of the given string
firstHalf = "" 
# second half of the given string
secondHalf = ""
# holds the reversed string
reversedString = ""

# if the length of the given string is even
if length%2 == 0 :
    firstHalf = string[0: half]
    secondHalf = string[half: length]
    print("firsthalf of the given string : {}".format(firstHalf))
    print("secondhalf of the given string : {}".format(secondHalf))
    
    if firstHalf == secondHalf :
        print("The given string : {} : is symmetrical.".format(string))
    else :
        print("The given string : {} : is not symmetrical.".format(string))
        
    
    # to store the reversed string
    for i in string :
        reversedString = i + reversedString
    
    # to check if the given string is palindrome or not
    if reversedString == string :
        print("The given string : {} : is a palindrome.".format(string))
    else :
        print("The given string : {} : is not a palindrome.".format(string))
        
# if the length of the stirng is odd 
elif length%2 != 0 :
    firstHalf = string[0: half]
    secondHalf = string[half+1: length] # after excluding the middle character for the string.
    print("firsthalf of the given string : {}".format(firstHalf))
    print("secondhalf of the given string : {}".format(secondHalf))
    
    if firstHalf == secondHalf :
        print("The given string : {} : is symmetrical.".format(string))
    else :
        print("The given string : {} : is not symmetrical.".format(string))
    
    
    # to store the reversed string
    for i in string : 
        reversedString = i + reversedString
    
    # to check if the given string is palindrome or not
    if reversedString == string :
        print("The given string : {} : is a palindrome.".format(string))
    else :
        print("The given string : {} : is not a palindrome.".format(string))