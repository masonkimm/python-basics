# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name = 'Sarah', last_name= 'Connor')


# Get value
# print(person['first_name'])
# print(person.get('last_name')) # more common way

# Add key value
person['phone'] = '555-555-5555'

# Get dict keys
# print(person.keys())

# Get dict items
# print(person.items())

# Copy dict
person3 = person.copy()  # ...spread operator from es6
person3['city'] = 'boston'

# Remove item by key
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
# print(len(person3))

# List of dict
people = [
    {'name': 'Black Widow', 'age': 30},
    {'name': 'Spider Man', 'age': 25},
    {'name': 'Iron Man', 'age': 40}
]

print(people, type(people))
print(people[1]['name'])

# print(person, type(person))
