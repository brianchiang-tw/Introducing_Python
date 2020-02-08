
class Duck():

    def __init__(self, input_name):

        self.hidden_name = input_name

    @property
    def name(self):

        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):

        print('inside the setter')
        self.hidden_name = input_name


def test_bench():


    

    fowl = Duck('Howard')
    
    # expected output:
    '''
    inside the getter
    Howard
    '''
    print( fowl.name )

    # expected output:
    '''
    inside the setter
    '''
    fowl.name = 'Donald'

    # expected output:
    '''
    inside the getter
    Donald
    '''
    print( fowl.name )



if __name__ == '__main__':

    test_bench()