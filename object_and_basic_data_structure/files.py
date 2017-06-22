# one can use python to interact with files

# for example one can create a file with the following

myfile = open('testfile.txt', 'w+')

# and add lines to it as follows

myfile.write('Hello World')
myfile.write('This is our new text myfile')
myfile.write('and this is another line.')
myfile.write('Why? Because we can.')

myfile.close()


for line in open('testfile.txt'):    
    print line
