# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_hd = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile_hd.name)
print('Is Closed : ', myFile_hd.closed)
print('Opening Mode: ', myFile_hd.mode)

# Write to file
myFile_hd.write('Dreams inspire action.')
myFile_hd.write(' Embrace change!')
myFile_hd.close()

# Append to file
myFile_hd = open('myfile.txt', 'a')
myFile_hd.write(' Believe in yourself always!')
myFile_hd.close()

# Read from file
myFile_hd = open('myfile.txt', 'r+')
text_hd = myFile_hd.read(100)
print(text_hd)
