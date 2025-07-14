# Turples in python
# Tuples are immutable sequences, typically used to store collections of heterogeneous items.
# They can contain items of different data types and are defined by parentheses.
# Different from lists, tuples cannot be modified after creation.
# creating and accessing elements in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing the first element
print(my_tuple[1])  # Accessing the second element
print(my_tuple[-1])  # Accessing the last element
# slicing a tuple
print(my_tuple[1:4])  # Slicing the tuple to get elements from index 1 to 3
# iterating through a tuple
for item in my_tuple:
    print(item)  # Display each item in the tuple
# checking if an element exists in a tuple
print(5 in my_tuple)  # Check if 5 is in the tuple
# counting occurrences of an element in a tuple
print(my_tuple.count(2))  # Count occurrences of 2 in the tuple
# finding the index of an element in a tuple
print(my_tuple.index(3))  # Get the index of the first occurrence of 3
# unpacking a tuple
a, b, c, d, e = my_tuple  # Unpacking the tuple into variables
print(a, b, c, d, e)  # Display the unpacked variables
# length of a tuple
print(len(my_tuple))  # Get the length of the tuple
# converting a list to a tuple
my_list = [1, 2, 3]
my_tuple_from_list = tuple(my_list)  # Convert list to tuple
print(my_tuple_from_list)  # Display the tuple created from the list
# converting a tuple to a list
my_tuple = (1, 2, 3)
my_list_from_tuple = list(my_tuple)  # Convert tuple to list
print(my_list_from_tuple)  # Display the list created from the tuple
# checking if a tuple is empty
empty_tuple = ()  # Creating an empty tuple
print(len(empty_tuple) == 0)  # Check if the tuple is empty
# checking if a tuple is not empty
print(len(my_tuple) > 0)  # Check if the tuple is not empty
# checking if a tuple is equal to another tuple
another_tuple = (1, 2, 3)
print(my_tuple == another_tuple)  # Check if the tuples are equal
