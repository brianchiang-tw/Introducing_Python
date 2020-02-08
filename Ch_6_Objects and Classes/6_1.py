class Thing:
    pass


def test_bench():
    '''
    Demo class and object
    '''


    # expected output:
    '''
    <class '__main__.Thing'>
    '''
    print( Thing )

    # expected output:
    # Note: the address could be different on each computer
    '''
    <__main__.Thing object at 0x000001EBCC042EF0>
    '''
    example = Thing()

    print( example )


if __name__ == '__main__':
    help(test_bench)
    test_bench()