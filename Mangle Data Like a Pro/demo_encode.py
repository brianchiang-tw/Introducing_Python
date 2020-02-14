snowman = '\u2603'

print( len(snowman) )

utf_bytecode = snowman.encode('utf-8')

print( len(utf_bytecode) )

# b'\xe2\x98\x83'
print( utf_bytecode )



