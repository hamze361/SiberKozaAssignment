# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_hd = 'Hamze'
age_hd = 21

# Concatenate
print('Hello, my name is ' + name_hd + ' and I am ' + str(age_hd))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name_hd, age=age_hd))

# F-Strings (3.6+)
print(f'Hello, my name is {name_hd} and I am {age_hd}')

# String Methods

s_hd = 'helloworld'

# Capitalize string
print(s_hd.capitalize())

# Make all uppercase
print(s_hd.upper())

# Make all lower
print(s_hd.lower())

# Swap case
print(s_hd.swapcase())

# Get length
print(len(s_hd))

# Replace
print(s_hd.replace('world', 'everyone'))

# Count
sub_hd = 'h'
print(s_hd.count(sub_hd))

# Starts with
print(s_hd.startswith('hello'))

# Ends with
print(s_hd.endswith('d'))

# Split into a list
print(s_hd.split())

# Find position
print(s_hd.find('r'))

# Is all alphanumeric
print(s_hd.isalnum())

# Is all alphabetic
print(s_hd.isalpha())

# Is all numeric
print(s_hd.isnumeric())
