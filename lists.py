# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_hd = [6, 7, 8, 9, 10]
fruits_hd = ['Bananas', 'Kiwis', 'Strawberries', 'Raspberries']

# Use a constructor
numbers2_hd = list((6, 7, 8, 9, 10))

# Get a value
print(fruits_hd[1])

# Get the last value
print(fruits_hd[-1])



# Get length
print(len(fruits_hd))

# Append to list
fruits_hd.append('Blackberries')

# Remove from list
fruits_hd.remove('Strawberries')

# Insert into position
fruits_hd.insert(2, 'Pineaplle')

# Change value
fruits_hd[0] = 'Lemon'

# Remove with pop
fruits_hd.pop(2)

# Reverse list
fruits_hd.reverse()

# Sort list
fruits_hd.sort()

# Reverse sort
fruits_hd.sort(reverse=True)

print(fruits_hd)
