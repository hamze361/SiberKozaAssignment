# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person_hd = {
    'first_name': 'Hamze',
    'last_name': 'Daher',
    'age': 21
}

# Use constructor
person2_hd = dict(first_name='Emma', last_name='Johnson')

# Get value
print(person_hd['first_name'])
print(person_hd.get('last_name'))

# Add key/value
person_hd['phone'] = '552-710-73-25'

# Get dict keys
print(person_hd.keys())

# Get dict items
print(person_hd.items())

# Copy dict
person2_hd = person2_hd.copy()
person2_hd['city'] = 'Toronto'

# Remove item
del(person_hd['age'])
person_hd.pop('phone')

# Clear
person_hd.clear()

# Get length
print(len(person2_hd))

# List of dict
people_hd = [
    {'name': 'David', 'age': 35},
    {'name': 'Sarah', 'age': 28}
]

print(people_hd[1]['name'])
