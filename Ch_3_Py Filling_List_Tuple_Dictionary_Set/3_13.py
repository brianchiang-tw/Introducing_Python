# dictionay, from English to French
e2f = { 'dog':'chien', 'cat': 'chat', 'walrus':'morse'}

# expected output:
'''
e2f: {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
'''
print( f'e2f: {e2f}' )


# dictionary, from French to English
f2e = { value:key for key, value in e2f.items() }

# expected output:
'''
f2e["chien"]: dog
'''
print( f'f2e["chien"]: {f2e["chien"]}' )