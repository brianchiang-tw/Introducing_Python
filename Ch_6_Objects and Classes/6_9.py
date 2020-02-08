
class Bear():

    animal_type = 'Bear'
    food = 'berries'

    def who(self):
        return Bear.animal_type

    def eats(self):
        return Bear.food



class Rabbit():

    animal_type = 'Rabbit'
    food = 'clover'

    def who(self):
        return Rabbit.animal_type
    
    def eats(self):
        return Rabbit.food


class Octothorpe():

    animal_type = 'Octothorpe'
    food = 'camper'

    def who(self):
        return Octothorpe.animal_type
    
    def eats(self):
        return Octothorpe.food



def animal_eat( obj_list ):

    for obj in obj_list:
        print( f'{obj.who()} eats {obj.eats()}')



def test_bench():
    '''
    Demo polymorphism and duck-typing
    '''

    obj_b = Bear()
    obj_r = Rabbit()
    obj_o = Octothorpe()

    obj_list = [ obj_b, obj_r, obj_o ]

    # expected output:
    '''
    Bear eats berries
    Rabbit eats clover
    Octothorpe eats camper
    '''

    animal_eat( obj_list )



if __name__ == '__main__':

    test_bench()