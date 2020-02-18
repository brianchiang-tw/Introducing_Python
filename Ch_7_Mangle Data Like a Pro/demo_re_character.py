import string
import re

printable = string.printable

# 100
print( len(printable) )

# b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN'
print( printable[:50].encode() )

# b'OPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
print( printable[50:].encode() )

number_character = re.findall('\d', printable )
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print( number_character )

number_alphabet_underline_character = re.findall('\w', printable)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
#  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
#  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
#  'Y', 'Z', '_']
print( number_alphabet_underline_character )

white_space_character = re.findall('\s', printable )
# [' ', '\t', '\n', '\r', '\x0b', '\x0c']
print( white_space_character )

# ----------------------------------------------

test_string = 'abc' + '-/*' + '\u00ea' + '\u0115'

alphabet = re.findall('\w', test_string )
# ['a', 'b', 'c', 'ê', 'ĕ']
print( alphabet )