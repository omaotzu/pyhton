# dictionaries are ruby hashes or javascript objects

# however... drawing on that data or creating it is done much more easily

obj = {}


obj['hello'] = 'world'


print(obj)


# you can store multiple datatypes in these as well eg


obj['arr'] = [1,2,3,4,5,6]

print(obj)

# and to access the indexed locations of these you can do the following


print(obj['arr'][0]) #which will return the zero index location in this array


# you can even go so far as to do the follow

obj['obj'] ={
    'first': 1,
    'second': 2,
    'third': {
        'embebbedd1': 'first embedded',
        'embebbedd3': 'second embedded'
    }
}

# to access this you can string the square brackets together to get this

print(obj['obj']['third']['embebbedd1']) #which prints its value 'first embedded'
