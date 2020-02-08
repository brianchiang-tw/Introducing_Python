
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



    def dump( self ):

        print( str(self) )


def test_bench():
    '''
    Demo instance method
    '''
    hydro_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
    hydrogen = Element( **hydro_dict )

    # expected output:
    '''
    Element name: Hydrogen
    Element symbol: H
    Element number: 0
    '''
    hydrogen.dump()



if __name__ == '__main__':

    help( test_bench )
    test_bench()