# Dictionaries in python
# Dictionaries are mutable mappings, typically used to store collections of key-value pairs.
# They are defined by curly braces and can contain items of different data types.
# creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
# accessing elements in a dictionary
print(my_dict['name'])  # Accessing the value associated with the key 'name'
print(my_dict.get('age'))  # Accessing the value associated with the key 'age'
# adding or updating elements in a dictionary
my_dict['age'] = 31  # Updating the value associated with the key 'age'
my_dict['country'] = 'USA'  # Adding a new key-value pair
# removing elements from a dictionary
del my_dict['city']  # Removing the key-value pair with key 'city'
# iterating through a dictionary
for key, value in my_dict.items():
    print(key, value)  # Display each key-value pair you can also use string literals
# checking if a key exists in a dictionary
print('name' in my_dict)  # Check if 'name' is a key in the dictionary
# getting the keys and values of a dictionary
print(my_dict.keys())  # Get a view of the dictionary's keys
print(my_dict.values())  # Get a view of the dictionary's values
# getting the length of a dictionary
print(len(my_dict))  # Get the number of key-value pairs in the dictionary
# clearing a dictionary
my_dict.clear()  # Remove all key-value pairs from the dictionary