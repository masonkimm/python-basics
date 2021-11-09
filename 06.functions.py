# A FUNCTION is a...
# block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Super Man'):
    print(f'Hello {name}')


sayHello('Wakanda')
sayHello()

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total


totalNum = getSum(2, 4)
print(totalNum)


# A LAMBDA FUNCTION is a...
# small anonymous function. It can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# getSum2 = lambda num1, num2 : num1 + num2

# print(getSum2(10, 3))
