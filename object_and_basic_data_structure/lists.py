# Lists are python arrays - like before if you want to convert a string to a list use the following command

print(list('Hello'))

list1 = ['h', 'e', 'l', 'l', 'o']


#.push() equivalent
list1.append(4)
print(list1)


# pop() still the same but you can remove specific index locations within a list by putting it in the parenthesis


list1.pop(0)
print(list1)


# if you leave the parenthesis blank it will remove the last element of the list

popped = list1.pop()

print(popped)#will display 4 as we appended it earlier

print(list1)#will display the list with the 4 removed



numbers_list = [1, 10, 2, 34, 121312312]

new_array = sorted(numbers_list)
# or numbers_list.sort()
print(numbers_list)

print(new_array)


# you can nests lists inside of one another as well to have lists within lists

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

concatList = [list1, list2, list3]

print(concatList)

# now if you want to used the index locations in the concatonated list it will return the list that is in that index location so concatList[0] will return [1,2,3] etc etc


# you can use a for loop to itterate through each of the 0 indexed locations of each of the lists to return a new array with these in
first_col = [row[0] for row in concatList]

print(first_col)
# will return [1,4,7] index 0 from list1 2 and 3
