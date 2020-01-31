
guess_me = 7

start = 1

# expected output:
'''
too low
too low
too low
too low
too low
too low
found it!
'''


while True:

    if start < guess_me:
        print('too low')

    elif start > guess_me:
        print('oops')

    else:
        print('found it!')
        break 

    start += 1