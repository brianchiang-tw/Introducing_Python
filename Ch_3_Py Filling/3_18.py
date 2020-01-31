

bottom_dict = { 'cats':['Henri','Grumpy','Lucy'], 'octopi':dict(), 'emus': dict() }
life = { 'animals': bottom_dict, 'plants': dict(), 'other': dict() }



# expected output:
'''
['Henri', 'Grumpy', 'Lucy']
'''
print( life['animals']['cats'] )