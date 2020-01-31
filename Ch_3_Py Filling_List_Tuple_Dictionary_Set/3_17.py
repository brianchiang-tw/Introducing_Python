

bottom_dict = { 'cats':['Henri','Grumpy','Lucy'], 'octopi':dict(), 'emus': dict() }
life = { 'animals': bottom_dict, 'plants': dict(), 'other': dict() }



# expected output:
'''
dict_keys(['cats', 'octopi', 'emus'])
'''
print( life['animals'].keys() )