from collections import OrderedDict

fancy = OrderedDict( )

fancy['a'] = 1
fancy['b'] = 2
fancy['c'] = 3

# expected output:
'''
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
'''
print( fancy )