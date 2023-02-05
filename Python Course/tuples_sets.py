# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
vegetables_hd = ('Carrots', 'Lettuces', 'Spinach')

# Using a constructor
vegetables2_hd = tuple(('Carrots', 'Lettuces', 'Spinach'))

# Single value needs trailing comma
vegetables2_hd = ('Carrots',)

# Get value
print(vegetables_hd[1])

# Can't change value
vegetables_hd[0] = 'Potatoes'

# Delete tuple
del vegetables2_hd

# Get length
print(len(vegetables_hd))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
vegetables_set_hd = {'Carrots', 'Lettuces', 'Spinaches'}

# Check if in set
print('Carrots' in vegetables_set_hd)

# Add to set
vegetables_set_hd.add('Onions')

# Remove from set
vegetables_set_hd.remove('Spinaches')

# Add duplicate
vegetables_set_hd.add('Carrots')

# Clear set
vegetables_set_hd.clear()

# Delete
del vegetables_set_hd

print(vegetables_set_hd)
