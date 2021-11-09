# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Import modules
import datetime
from datetime import date
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
from validator import validate_email


# Date way 1
today = datetime.date.today()
# print(today)

# Date way 2
today2 = date.today()
# print(today2)

# Time
timestamp = time()
# print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
