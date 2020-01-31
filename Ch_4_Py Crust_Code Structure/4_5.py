
# dictionary comprehension

square_value_dict = { x:x**2 for x in range(10) }

# expected output:
'''
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
'''
print( square_value_dict )