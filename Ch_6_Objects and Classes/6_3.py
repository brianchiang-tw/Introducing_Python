
class Thing3():

    def __init__(self):

        self.letters = ''



def test_bench():
    '''
    Demo instance attribute
    '''

    # expected output:
    '''
    AttributeError: type object 'Thing3' has no attribute 'letters'
    '''

    try:
        print( Thing3.letters)

    except AttributeError as err:
        print(f'AttributeError: {err}' )



    instance = Thing3()
    instance.letters = 'xyz'

    # expected output:
    '''
    xyz
    '''
    print( instance.letters )



if __name__ == '__main__':

    help(test_bench)
    test_bench()