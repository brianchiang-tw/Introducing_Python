hexstring = '47494638396101000100800000000000ffffff21f9' + \
            '0401000000002c000000000100010000020144003b'

import binascii

bytes_data = binascii.unhexlify( hexstring )


# b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;
#print( bytes_data )

# <class 'bytes'>
#print( type(bytes_data) )

import struct

img_w, img_h = struct.unpack('<H', bytes_data[6:8])[0], struct.unpack('<H', bytes_data[8:10])[0]

# image width 1
# image height 1
print(f'image width {img_w}\nimage height {img_h}')