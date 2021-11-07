# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))


# Get a value
print(fruits[0])  # => oranges

# Get length
print(len(fruits))  # => 4

# Append (add to the end of the list)
fruits.append('Mangoes')
print(fruits)

# Insert (add to specific index)
fruits.insert(0, "Strawberries")
print(fruits)

# Change value
fruits[0] = "Blueberries"
print(fruits)

# Remove (with name)
fruits.remove("Grapes")
print(fruits)

# Remove (with index)
fruits.pop(0)
print(fruits)

# Reverse
fruits.reverse()
print(fruits)

# Sort (a-z)
fruits.sort()
print(fruits)

# Sort (z-a)
fruits.sort(reverse=True)
print(fruits)
