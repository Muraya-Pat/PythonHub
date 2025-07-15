# Conditional statements and control flow in Python
# Conditional statements allow you to execute code based on certain conditions.
# In python various conditional statements are used such as if, elif, and else.
# Example of if statement
x = 10
if x > 5:
    print("x is greater than 5")  # This block executes if the condition is true
# Example of if-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is greater than or equal to 5")
# Example of if-elif-else statement
if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5")
# Nested if statements
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")  # This block executes if x is positive and even
    else:
        print("x is odd")  # This block executes if x is positive and odd

# control flow with logical operators
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")  # This block executes if both conditions are true
if x < 5 or y > 15:
    print("At least one of the conditions is true")  # This block executes if either condition is true
# Using the not operator
if not (x < 5):
    print("x is not less than 5")  # This block executes if the condition is false
# Ternary operator for conditional assignment
z = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(z)  # Display the result of the ternary operation

# Using conditional statements in loops
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")  # This block executes for even numbers
    else:
        print(f"{i} is odd")  # This block executes for odd numbers
# Using conditional statements with functions
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"