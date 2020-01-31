# dictionay, from English to French
e2f = { 'dog':'chien', 'cat': 'chat', 'walrus':'morse'}



words = { key for key in e2f}


# expected output:
'''
type(words): <class 'set'>
words: {'walrus', 'cat', 'dog'}
'''

print( f'type(words): {type(words)}' )
print( f'words: {words}' )