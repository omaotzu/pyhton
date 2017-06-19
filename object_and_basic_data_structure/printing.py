# use %s to insert variables into strings similar to ${} in javascript eg:

string = 'Omar'

print('Hello there %s' %(string))


# Floating point numbers are used to print specific lengths of strings inserting white space where necessary and how many after a decimal places


# Its taken in the format of %10.3f where before the decimal point is the length of the string and after the decimal point is how many digits after the decimal point

# eg
number = 30.123456789
print('Testing %20.2f' %(number))
# This prints: Testing                30.12

print('Testing %30.2f' %(number))
# This prints: Testing                          30.12

print('Testing %20.4f' %(number))
# This prints: Testing              30.1235


# Instead of %s you can also use %r and it will work with numbers or strings, this will be covered later in the course in more detail though

# eg

a = 123.22
b = 'Hello world'

print('Example a %s, example b %r' %(a, b))

# Will print the same as me using either of the following
print('Example a %r, example b %r' %(a, b))
print('Example a %s, example b %s' %(a, b))


# you can once again use format to add in whatever you want
print 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')
print 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3)
