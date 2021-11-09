# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


people = ['Spider Man', 'Iron Man', 'Batman', 'Superman']

# Simple for-loop
# for person in people:
# print (f'Current person: {person}')

# Break
# for person in people:
#   if person == 'Batman':
#     break # will stop before 'Batman'
#   print(f'Current person: {person}')

# Continue
# for person in people:
#   if person == 'Batman':
#     continue # will skip 'Batman' and continue on
#   print(f'Current person: {person}')

# # Range
# for i in range(len(people)):
#   print(people[i])

# for i in range(0, 11): # 0-10
#   print(f'Number : {i}')


# While loops execute a set of statements as long as a condition is true.

count = 0
# 0-10
# while count <= 10:
#     print(f'Count: {count}')
#     count += 1
# 0-9
while count < 10:
    print(f'Count: {count}')
    count += 1
