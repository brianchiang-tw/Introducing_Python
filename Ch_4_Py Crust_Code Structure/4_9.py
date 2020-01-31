
# generator for odd number within 10
def get_odds():

    for i in range(1,10,2):
        yield(i)



# expected output:
'''
5
'''

ranger = get_odds()
for index, odd in enumerate(ranger):

    if index == 2:
        print( odd )
        