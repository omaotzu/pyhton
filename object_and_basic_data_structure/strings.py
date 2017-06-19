# len function for length
print(len('Hello'))

string = 'Hello'

# Print second index location
print(string[1])
# Print everything from index location to end of string
print(string[1:])

# Print everything before given index location
print(string[:3])

# If unknown length -- can loop backwards and print specific index location from end of array by using minus
print(string[-1])


# Print everything except for last letter  --- this is so cool
print(string[:-1])

# Print every second index location in a string
print(string[::2])

# Print entire string in reverse
print(string[::-1])

# Print every second index location in reverse
print(string[::-2])

# Reassign entire strings
string = string +'!'
print(string)

# can use repetition as follows
sleepy = 'z'

print(sleepy*10)

# uppercase
print(string.upper())

# lowercase
print(string.lower())

# split method at specific letter - will not include the letter in either index of the new array
print(string.split('e'))

# create an array from a string
print(list(string))

# Insert into specific point in string by using format and changing whatever is in the curly brackets
print('Hello {} - nice to meet you'.format('Omar'))
