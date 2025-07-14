# Lists in python
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# They can contain items of different data types and are defined by square brackets.
# creating and accessing elements in a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing the first element
print(my_list[1])  # Accessing the second element
print(my_list[-1])  # Accessing the last element

# modifying elements in a list
my_list[0] = 10  # Changing the first element
print(my_list)  # Display the modified list
# adding elements to a list
my_list.append(6)  # Adding an element to the end of the list
print(my_list)  # Display the list after adding an element
# removing elements from a list
my_list.remove(3)  # Removing an element from the list
print(my_list)  # Display the list after removing an element
# slicing a list
print(my_list[1:4])  # Slicing the list to get elements from index 1 to 3
# iterating through a list
for item in my_list:
    print(item)  # Display each item in the list
# sorting a list
my_list.sort()  # Sorting the list in ascending order
print(my_list)  # Display the sorted list
# reversing a list
my_list.reverse()  # Reversing the order of elements in the list
print(my_list)  # Display the reversed list
# checking if an element exists in a list
print(5 in my_list)  # Check if 5 is in the list
# pop method
popped_item = my_list.pop()  # Remove and return the last item
print(popped_item)  # Display the popped item
