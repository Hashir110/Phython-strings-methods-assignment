# Converts the first character to upper case

# method1 = "hi, i am muhammad hashir."

# x = method1.capitalize()

# print (x)

# Make the string lower case:

# method2 = "Hello, And Welcome To My World!"

# x = method2.casefold()

# print(x)
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

# method3 = "programmer"

# x = method3.center(20)

# print(x)

# Return the number of times the value "apple" appears in the string:

# method4 = "lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem! Autem, quae. Iure, quidem? Quisquam, quidem! Autem, quae. Iure, quidem?"

# x = method4.count("Autem")

# print(x)

# UTF-8 encode the string:

# method5 = "my name is håshir"

# x = method1.encode()

# print(x)

# Check if the string ends with a punctuation sign (.):

# method6 = "Hello, welcome to my world."

# x = method6.endswith(".")

# print(x)

# Set the tab size to 2 whitespaces:

# method7 = "H\te\tl\tl\to"

# x =  method7.expandtabs(2)

# print(x)

# Where in the text is the word "welcome"?:

# method8 = "Hello, welcome to my world."

# x = method8.find("welcome")

# print(x)

# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

# method9 = "For only {price:.2f} dollars!"
# print(method9.format(price = 49))

# nsert the name and age from a dictionary into the placeholders.

# myvar = {"name" : "Muhammad Hashir", "age" : 19}
# method10 = "Happy birthday {name} you are now on level {age}!"
# print(method10.format_map(myvar))

# Where in the text is the word "welcome"?:

# method11 = "Hello, welcome to my world."

# x = method11.index("welcome")

# print(x)

# Check if all the characters in the text are alphanumeric:

# method12 = "Company12"

# x = method12.isalnum()

# print(x)

# Check if all the characters in the text are letters:

# method13 = "CompanyX"

# x = method13.isalpha()

# print(x)

# Check if all the characters in the text are ascii characters:

# method14 = "Company123"

# x = method14.isascii()

# print(x)

# Check if all the characters in a string are decimals (0-9):

# method15 = "1234"

# x = method15.isdecimal()

# print(x)

# Check if all the characters in the text are digits:

# method16 = "50800"

# x = method16.isdigit()

# print(x)

# Check if the string is a valid identifier:

# method18 = "Demo"

# x = method18.isidentifier()

# print(x)

# Check if all the characters in the text are in lower case:

# method19 = "hello world!"

# x = method19.islower()

# print(x)

# Check if all the characters in the text are numeric:

# method20 = "565543"

# x = method20.isnumeric()

# print(x)

# Check if all the characters in the text are printable:

# method21 = "Hello! Are you #1?"

# x = method21.isprintable()

# print(x)

# Check if all the characters in the text are whitespaces:

# method22 = "   "

# x = method22.isspace()

# print(x)

# Check if each word start with an upper case letter:

# method23 = "Hello, And Welcome To My World!"

# x = method23.istitle()

# print(x)

# Check if all the characters in the text are in upper case:

# method24 = "THIS IS NOW!"

# x = method24.isupper()

# print(x)

# Join all items in a tuple into a string, using a hash character as separator:

# myTuple = ("Hashir", "Ayein", "Hamza")

# x = "-".join(myTuple)

# print(x)

# Return a 20 characters long, left justified version of the word "hashir":

# method25 = "hashir"

# x = method25.ljust(20)

# print(x, "is my favorite fruit.")

# Lower case the string:

# method26 = "Hello my FRIENDS"

# x = method26.lower()

# print(x)

# Remove spaces to the left of the string:

# method27 = "     apple     "

# x = method27.lstrip()

# print("of all fruits", x, "is my favorite")

# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:

# method28 = "Hello Sashir!"
# mytable = str.maketrans("S", "H")
# print(method28.translate(mytable))

# Search for the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

# method29 = "I could eat bananas all day"

# x = method29.partition("bananas")

# print(x)

# Replace the word "bananas":

# method30 = "I like mango"

# x = method30.replace("mango", "apple")

# print(x)

# Where in the text is the last occurrence of the string "casa"?:

# method31 = "Mi casa, su casa."

# x = method31.rfind("casa")

# print(x)

# Split a string into a list, using comma, followed by a space (, ) as the separator:

# method32 = "apple, banana, cherry"

# x = method33.rsplit(", ")

# print(x)

# Split a string into a list where each word is a list item:

# method34 = "welcome to the jungle"

# x = method34.split()

# print(x)

# Split a string into a list where each line is a list item:

# method35 = "Thank you for the music\nWelcome to the jungle"

# x = method35.splitlines()

# print(x)

# Check if the string starts with "Hello":

# method36 = "Hello, welcome to my world."

# x = method36.startswith("Hello")

# print(x)

# Remove spaces at the beginning and at the end of the string:

# method37 = "     banana     "

# x = method37.strip()

# print("of all fruits", x, "is my favorite")

# Make the lower case letters upper case and the upper case letters lower case:

# method38 = "Hello My Name Is HASHIR"

# x = method38.swapcase()

# print(x)

# Make the first letter in each word upper case:

# method39 = "Welcome to my world"

# x = method39.title()

# print(x)

# Replace any "S" characters with a "P" character:

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83: 80}
# method40 = "Hello Sam!"
# print(method40.translate(mydict))

# Upper case the string:

# method41 = "Hello my friends"

# x = method41.upper()

# print(x)

# Fill the string with zeros until it is 10 characters long:

# method42 = "50"

# x = method42.zfill(10)

# print(x)