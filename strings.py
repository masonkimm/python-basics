# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# ---- Concatenate ----

name = 'Jennifer'
age = 31

# Error => cannot combine str + int
'''
print('Hello ' + name + 'age: ' + age) 
'''
print('Hello my name is ' + name + ' and I am ' + str(age))


# ---- String Formatting ----

# Argument by position
print('Hello My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings
print(f'Hello my name is {name} and I am {age}')


# ---- String Methods ----

s = 'hello world'
t = 'meta'

# Capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case => change to opposite
print(s.swapcase())

# Get length
print(len(s))

# Replace world => everyone
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list => []
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())
print(t.isalnum())

# Is all aphabetic
print(s.isalpha())
print(t.isalpha())

# Is all numeric
print(s.isnumeric())
print(t.isnumeric())
