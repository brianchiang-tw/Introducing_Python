def unicode_test( value ):

    import unicodedata

    name = unicodedata.name( value )
    value2 = unicodedata.lookup( name )

    print(f'original data: {value}, unicode name: {name}, turn it back: {value2}')



def test_bench():

    test_data = [
                    'A',
                    '$',
                    '\u00a2',
                    '\u20ac',
                    '\u2603'
                ]
        
    for character in test_data:

        print( unicode_test(character) )
    
    return 



if __name__ == '__main__':

    test_bench()