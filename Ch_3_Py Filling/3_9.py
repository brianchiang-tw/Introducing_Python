

surprise = []

surprise.append( 'Groucho' )
surprise.append( 'Chico' )
surprise.append( 'Harpo' )

# expected output:
'''
['Groucho', 'Chico', 'Harpo']
'''
print( surprise )


surprise[-1] = surprise[-1].lower()

surprise[-1] = surprise[-1][::-1]

# expected output:
'''
['Groucho', 'Chico', 'oprah']
'''
print( surprise )

surprise[-1] = surprise[-1].capitalize()

# expected output:
'''
['Groucho', 'Chico', 'Oprah']
'''
print( surprise )