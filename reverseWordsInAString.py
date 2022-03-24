# python program to reverse the words given in a string
# to take user defined input string
string = input("Enter a random string: ") 
# split the given string into words using the split function
words = string.split(" ")
# initializing the reverseWords variable to hold the reversedString value
reversedWords = ""

# iterate over every word and reverse them 
for word in words : 
    # placing space after every word.
    reversedWords = word + " " + reversedWords 

# using the strip() function to remove the additional spaces from start and the end of the given string
reversedWords.strip()
# print the reversed string
print(reversedWords)