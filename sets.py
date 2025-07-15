# sets in Python
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.
# creating a set
my_set = {1, 2, 3, 4, 5}
# accessing elements in a set
# Sets do not support indexing because they are unordered, but you can check for membership
print(3 in my_set)  # Check if 3 is in the set
print(6 in my_set)  # Check if 6 is in the set
# adding elements to a set
my_set.add(6)  # Adding an element to the set
print(my_set)  # Display the set after adding an element
# removing elements from a set
my_set.remove(2)  # Removing an element from the set
print(my_set)  # Display the set after removing an element
# using discard method
my_set.discard(4)  # Discarding an element (does not raise an error if the element is not found)
print(my_set)  # Display the set after discarding an element
# iterating through a set
for item in my_set:
    print(item)  # Display each item in the set

# Sets are mainly used for membership testing and eliminating duplicate entries.
# Sets eliminaate duplicate entries automatically by their nature.