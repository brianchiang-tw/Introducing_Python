
class Element():

    def __init__( self, name, symbol, number):

        self.name = name
        self.symbol = symbol
        self.number = 0

    def __str__(self):

        print_str = [
                        f'Element name: {self.name}', 
                        f'Element symbol: {self.symbol}', 
                        f'Element number: {self.number}'
                    ]

        return '\n'.join( print_str )


def test_bench():
    '''
    Demo instance attribute
    '''

    hydrogen = Element('Hydrogen','H', 1)

    # expected output:
    '''
    Element name: Hydrogen
    Element symbol: H
    Element number: 0
    '''
    print( hydrogen )



if __name__ == '__main__':
    help( test_bench )
    test_bench()