from collections import defaultdict

# default value will be empty list
dict_of_lists = defaultdict( list )

dict_of_lists['a'].append( 'something for a')

print( dict_of_lists['a'] )