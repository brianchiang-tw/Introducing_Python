
class Thing2():

    # class attribute
    letters = 'abc'
    


def test_bench():
    '''
    Demo class attribute
    '''


    # expected output:
    '''
    abc
    '''
    print( Thing2.letters )



if __name__ == '__main__':
    help( test_bench )
    test_bench()
