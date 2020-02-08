
class Element():

    def __init__( self, name, symbol, number):

        #print( kwargs )

        self.__name = name
        self.__symbol = symbol
        self.__number = 0

    def __str__(self):

        print_str = [
                        f'Element name: {self.__name}', 
                        f'Element symbol: {self.__symbol}', 
                        f'Element number: {self.__number}'
                    ]

        return '\n'.join( print_str )



    def dump( self ):

        print( str(self) )


    @property
    def name(self):
        return f'Element name: {self.__name}'

    @property
    def symbol(self):
        return f'Element symbol: {self.__symbol}'
    
    @property
    def number(self):
        return f'Element number: {self.__number}'



def test_bench():
    '''
    Demo instance private attribute and decorator
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