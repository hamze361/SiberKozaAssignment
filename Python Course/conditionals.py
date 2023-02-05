# If/ Else conditions are used to decide to do something based on something being true or false

x_hd = 22
y_hd = 21

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_hd > y_hd:
    print(f'{x_hd} is greater than {y_hd}')

# If/else
if x_hd > y_hd:
    print(f'{x_hd} is greater than {y_hd}')
else:
    print(f'{y_hd} is greater than {x_hd}')

# elif
if x_hd > y_hd:
    print(f'{x_hd} is greater than {y_hd}')
elif x_hd == y_hd:
    print(f'{x_hd} is equal to {y_hd}')
else:
    print(f'{y_hd} is greater than {x_hd}')

# Nested if
if x_hd > 3:
    if x_hd <= 11:
        print(f'{x_hd} is greater than 3 and less than or equal to 11')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_hd > 3 and x_hd <= 11:
    print(f'{x_hd} is greater than 3 and less than or equal to 11')

# or
if x_hd > 3 or x_hd <= 11:
    print(f'{x_hd} is greater than 3 or less than or equal to 11')

# not
if not (x_hd == y_hd):
    print(f'{x_hd} is not equal to {y_hd}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_hd = [6, 7, 8, 9, 10]

#  in
if x_hd in numbers_hd:
    print(x_hd in numbers_hd)

# not in
if x_hd not in numbers_hd:
    print(x_hd not in numbers_hd)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_hd is y_hd:
    print(x_hd is y_hd)

# is not
if x_hd is not y_hd:
    print(x_hd is not y_hd)
