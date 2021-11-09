# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
# if x > y:
#   print(f'{x} is greater than {y}')

# If/ else
# if x > y:
#   print(f'{x} is greater than {y}')
# else:
#   print(f'{x} is less than {y}')

# Elif
# if x > y:
#   print(f'{x} is greater than {y}')
# elif x == y:
#   print(f'{x} is equal to {y}')
# else:
#   print(f'{x} is less than {y}')

# Nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# # And => both true
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than or equal to 10')
# # Or => only one has to be true
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 or but less than or equal to 10')
# # Not
# if not(x == y):
#     print(f'{x} does not equal {y}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object


# numbers = [1,2,3,4,5]

# if x in numbers:
# 	print(x in numbers)
# 	print(f'{x} is in numbers')

# if y not in numbers:
# 	print(y not in numbers)
# 	print(f'{y} is not in numbers')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Is
if x is y:
    print(x is y)

# Is not
if x is not y:
    print(x is not y)
