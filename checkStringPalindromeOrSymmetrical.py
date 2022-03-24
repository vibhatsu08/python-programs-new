# python program to check if a given string is palindrome or symmetrical
string = input("Enter a random string : ")
length = len(string)
half = (length)//2

firstHalf = ""
secondHalf = ""
reversedString = ""

if length%2 == 0 :
    firstHalf = string[0: half]
    secondHalf = string[half: length]
    print("firsthalf of the given string : {}".format(firstHalf))
    print("secondhalf of the given string : {}".format(secondHalf))
    
    if firstHalf == secondHalf :
        print("The given string : {} : is symmetrical.".format(string))
    else :
        print("The given string : {} : is not symmetrical.".format(string))
        
    
    for i in string :
        reversedString = i + reversedString
    
    if reversedString == string :
        print("The given string : {} : is a palindrome.".format(string))
    else :
        print("The given string : {} : is not a palindrome.".format(string))
        
elif length%2 != 0 :
    firstHalf = string[0: half]
    secondHalf = string[half+1: length] # after excluding the middle character for the string.
    print("firsthalf of the given string : {}".format(firstHalf))
    print("secondhalf of the given string : {}".format(secondHalf))
    
    if firstHalf == secondHalf :
        print("The given string : {} : is symmetrical.".format(string))
    else :
        print("The given string : {} : is not symmetrical.".format(string))
    
    
    for i in string :
        reversedString = i + reversedString
    
    if reversedString == string :
        print("The given string : {} : is a palindrome.".format(string))
    else :
        print("The given string : {} : is not a palindrome.".format(string))