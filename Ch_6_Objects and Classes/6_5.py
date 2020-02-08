
class Element():

    def __init__( self, name, symbol, number):

        #print( kwargs )

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
    Demo instance initialization with dictionary
    '''
    hydro_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
    hydrogen = Element( **hydro_dict )

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