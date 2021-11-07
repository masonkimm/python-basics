# A TUPLE is... => ()
# a collection which is ordered and UNCHANGEABLE. Allows duplicate members.


# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

tuple = ('Apples',)  # needs a trailing comma
string = ('Apples')

# print(tuple, type(tuple))
# print(string, type(string))

# Get a value
print(fruits[1])

# TypeError: tuple does not support item assignment
# fruits[0] = 'Pears'

del fruits  # return error: not defined

# Get length
# print('length of fruits: ', len(fruits)) # return 3

# print(fruits)

# -------------------------------------------------

# A SET is... => {}
# a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Magngo'}
# print(fruits_set, type(fruits_set))

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')
# print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
# print(fruits_set)

# Clear the whole set
fruits_set.clear()

# Delete
del fruits_set  # return error: not defined

# print(fruits_set)
