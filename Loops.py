# Loops in python
# Loops are used to execute a block of code repeatedly.
# There are two main types of loops in Python: for loops and while loops.
# For loop
for i in range(5):  # Looping through a range of numbers from 0 to 4
    print(i)  # Display the current value of i
# While loop
count = 0  # Initializing a counter variable
while count < 5:  # Loop until count is less than 5
    print(count)  # Display the current value of count
    count += 1  # Increment count by 1
# Nested loops
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i: {i}, j: {j}")  # Display the current values of i and j
# Loop control statements
for i in range(5):
    if i == 2:
        break  # Break statement to exit the loop
    print(i)
# Continue statement
for i in range(5):
    if i == 2:
        continue  # Continue statement to skip the current iteration
    print(i)

# A complex and practical example of a nested loop
# This example demonstrates a multiplication table using nested loops
print("Multiplication Table:")
for i in range(1, 6):  # Outer loop for the first number
    for j in range(1, 6):  # Inner loop for the second number
        print(f"{i} x {j} = {i * j}")  # Display the multiplication result