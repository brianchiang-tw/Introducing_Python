

# generator expression
for demo_str in ( 'Got {}'.format(i) for i in range(10) ):

    print( demo_str )

# expected output
'''
Got 0
Got 1
Got 2
Got 3
Got 4
Got 5
Got 6
Got 7
Got 8
Got 9
'''