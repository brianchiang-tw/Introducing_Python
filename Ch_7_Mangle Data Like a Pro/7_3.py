mystery = '\U0001f4a9'

pop_bytes = mystery.encode('utf-8')

# b'\xf0\x9f\x92\xa9'
print( pop_bytes )

pop_string = pop_bytes.decode('utf-8')

# True
print( pop_string == mystery ) 