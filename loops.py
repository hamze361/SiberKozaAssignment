# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_hd = ['Edward', 'Levi', 'Maka', 'Denji']

# Simple for loop
for person_hd in people_hd:
  print(f'Current Person: {person_hd}')

# Break
for person_hd in people_hd:
  if person_hd == 'Maka':
    break
  print(f'Current Person: {person_hd}')

# Continue
for person_hd in people_hd:
  if person_hd == 'Sara':
    continue
  print(f'Current Person: {person_hd}')

# range
for i in range(len(people_hd)):
  print(people_hd[i])

for i in range(1, 12):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_hd = 1
while count_hd < 11:
  print(f'Count: {count_hd}')
  count_hd += 2
