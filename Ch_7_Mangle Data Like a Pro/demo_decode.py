place = 'caf\u00e9'

# café
print( place )

# <class 'str'>
print( type(place) )

place_bytes = place.encode('utf-8')

# b'caf\xc3\xa9'
print( place_bytes )

# <class 'bytes'>
print( type(place_bytes) )

place2 = place_bytes.decode('utf-8')

# café
print( place2 )