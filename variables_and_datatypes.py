#python variables and datatypes and type conversion
# Variables and Data Types
# Python supports various data types including integers, floats, strings, and booleans.
# Example of variables and data types
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True  # Boolean

# Type Conversion
# Python allows type conversion between different data types.
# Example of type conversion
x_str = str(x)  # Convert integer to string
y_int = int(y)  # Convert float to integer
name_int = int(len(name))  # Convert length of string to integer
# Displaying the variables and their types
print("Variables and Data Types:")
print(f"x: {x} (Type: {type(x)})")
print(f"y: {y} (Type: {type(y)})")
print(f"name: {name} (Type: {type(name)})")
print(f"is_student: {is_student} (Type: {type(is_student)})")
print("\nType Conversion:")