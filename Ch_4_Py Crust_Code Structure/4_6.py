
# set comprehension

odd_number_set = { x for x in range(10) if x % 2 == 1 }

# expected output:
'''
{1, 3, 5, 7, 9}
'''
print( odd_number_set )