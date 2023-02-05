# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x_hd = 2
y_hd = 3.6
name_hd = 'Hamze'
is_cool_hd = False

x_hd, y_hd, name_hd, is_cool_hd = (2, 3.6, 'Hamze', False)

a_hd = x_hd + y_hd

print(x_hd, y_hd, name_hd, is_cool_hd, a_hd)

x_hd = str(x_hd)
y_hd = int(y_hd)
z_hd = float(y_hd)

print(type(z_hd), z_hd)
