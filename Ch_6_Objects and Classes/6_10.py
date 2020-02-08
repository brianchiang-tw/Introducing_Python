
class Laser():

    def does(self):
        return 'disintegrate'

    def __name__(self):
        return 'Laser'

class Claw():

    def does(self):
        return 'crush'

    def __name__(self):
        return 'Claw'



class Smartphone():

    def does(self):
        return 'ring'

    def __name__(self):
        return 'Smartphone'




class Robot():

    def __init__(self):
        self.__laser = Laser()
        self.__claw = Claw()
        self.__smartphone = Smartphone()

    def does(self):

        functionality = [ 
                            f'{type(self.__laser).__name__}: {self.__laser.does()}',
                            f'{type(self.__claw).__name__}: {self.__claw.does()}',
                            f'{type(self.__smartphone).__name__}: {self.__smartphone.does()}'
                        ]
        print('Components:')
        print( '\n'.join(functionality) )



def test_bench():
    '''
    Demo of composition
    '''

    robot_obj = Robot()

    robot_obj.does()



if __name__ == '__main__':

    test_bench()
