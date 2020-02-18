import binascii

valid_png_header = b'\x89PNG\r\n\x1a\n'

# Hexify
# b'89504e470d0a1a0a'
print( binascii.hexlify(valid_png_header) )

# Unhexify
# b'\x89PNG\r\n\x1a\n'
print( binascii.unhexlify(b'89504e470d0a1a0a') )