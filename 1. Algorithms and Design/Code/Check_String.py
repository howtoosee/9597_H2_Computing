#check string:

user = input("Please enter a string: ")

if user.isalnum():
    print("The input contains only alphabetic letters or numerals.")

if user.isalpha():
    print("The input contains only alphabetic letters.")

if user.isdigit():
    print("The input contains only digits.")

if user.islower():
    print("The input contains only lower-cased alphabetical letters.")

if user.isupper():
    print("The input contains only upper-cased alphabetical letters.")

if user.isspace():
    print("The input contains only spaces.")

else:
    print("The input is an invalid string.")
