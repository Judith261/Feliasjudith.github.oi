# A program for you calculate the length of a string.
def length_of_string(s):
    return len(s)
string =input("Enter a String: ")
length = length_of_string(string)
print(f"The length of the string is: {length}\n")

#  A program count the number of characters in a string.

def count_numbers_of_string(s):
    return len(s)   
string =input("Enter a String: ")
char_count = count_numbers_of_string(string)
print(f"The number of character in the string is: {char_count}\n")

#A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 

def replace_character(s):
    return s[0] + s[1:].replace(s[0],'$')
string =input("Enter a String: ")
print("This is the modified String: "+ replace_character(string)+"\n")

#A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap_string_and_concatenate(word1,word2):
    return word2[:2]+ word1[2:] + '' + word1[:2]+ word2[2:]
word1 = input("Enter First Word: ")
word2 = input("Enter Second Word: ")
print("Result of Combine two word: " +swap_string_and_concatenate(word1,word2)+"\n")

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
firstname = 'Judith'
middlename = 'Bataycan'
lastname = 'Felias'
section = 'BSCS 3F'

concatenate = firstname + ' ' + middlename + ' ' + lastname  + ' ' + section
print(concatenate + '\n')

# Using + Concatenate Strings in Python get two strings from user input and concatenate them

string1 = input("Enter first word: ")
string2 = input("Enter second word: ")

result = string1 + ' ' + string2
print("Result of concatenate of two words: "+result+'\n')

# Using + Concatenate in Python using your name and your age in a paragraph
name = 'Judith Felias'
age = 21

result = "My Name is " + name + ' ' + "and, I'm " + str(age) + " Years Old"
print(result)
