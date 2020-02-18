import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'

data =  b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'


# expected output:
'''
Valid PNG width: 154, height: 141
'''
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24] )
    
    print(f'Valid PNG width: {width}, height: {height}')

else:
    print('Not a vliad PNG file')



## Pack python data type to byte
byte_data = struct.pack('>L', 154)
# b'\x00\x00\x00\x9a'
print( byte_data )

byte_data = struct.pack('>L', 141)
# b'\x00\x00\x00\x8d'
print( byte_data )

## Unpack bytes to python data
unpack_data = struct.unpack('>2L', data[16:24] )
# (154, 141)
print( unpack_data )

## Unpack bytes by direct addressing
unpack_data = struct.unpack('>16x2L6x', data )
# (154, 141)
print( unpack_data )