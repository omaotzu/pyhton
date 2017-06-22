# a tuple is immutable array or list that is denoted by brackets and seperating elements with commas

tup = (1,2,3)

print(tup)


# tuples have the some of the same methods as lists and can be indexed or sliced with tup[0] or tup[-1], however, the actual content of the tuple cant be changed

# one can find the index of a value by simply stating something like thos

t = ('zero', 'one', 'two', 'three')

print(t.index('one')) #which returns one

# you can use count to count the number of occurances of a value within a tuple


t1 = ('one', 'one', 'one', 'two', 'three')

# so

print(t1.count('one'))

# will print 3 as there are three 'one' s

# obvious being immutable it means that we cant reassign values so t1[0]= 'zero' will throw an error

# used far less but mainly used for fixed lists of data eg days of the week or months of the year... things that never ever change
