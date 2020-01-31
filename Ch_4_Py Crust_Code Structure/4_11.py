
class OopsException(Exception):
    pass



# expected output:
'''
Caught an oops
'''
try:
    raise OopsException

except:
    print('Caught an oops')



raise OopsException

# expected output:
'''
Traceback (most recent call last):
  File ".../Ch_4_Py Crust_Code Structure/4_11.py", line 5, in <module>
    raise OopsException
__main__.OopsException
'''

