# string methods in python
str1 = "Hello, World!"
print(str1.lower())  # Convert to lowercase
print(str1.upper())  # Convert to uppercase
print(str1.replace("World", "Python"))  # Replace substring
print(str1.split(", "))  # Split string into a list
#strip methods
print(str1.strip("!"))  # Remove leading and trailing characters by defaul it removes spaces but you can also pass any character that you want to remove and it will be removed
 #find methods
print(str1.find("World"))  # Find the index of a substring
#other string methods
print(str1.startswith("Hello"))  # Check if string starts with a substring
print(str1.endswith("!"))  # Check if string ends with a substring
print(str1.isalpha())  # Check if all characters are alphabetic
print(str1.isdigit())  # Check if all characters are digits
print(str1.capitalize())  # Capitalize the first character
print(str1.startswith("Hello"))  # Check if string starts with a substring
# count method
print(str1.count("o"))  # Count occurrences of a substring
# display index of a substring
print(str1.index("World"))  # Get the index of a substring, raises ValueError if not found
# display length of string
print(f"Length of string: {len(str1)}")  # Get the length of the string
#Display index of a character
print(str1.index("o"))  # Get the index of a character, raises ValueError if not found