
class A():

    # class member
    counter = 0

    def __init__(self):

        # update object counter of class A
        A.counter += 1
        self.hello()



    def hello(self):
        print(f'Hi. I am a object of class A with counter = {A.counter}')


    
    @classmethod
    def children(cls):

        print(f'class A has {A.counter} objects')



def test_bench():

    # expected output:
    '''
    Hi. I am a object of class A with counter = 1
    Hi. I am a object of class A with counter = 2
    Hi. I am a object of class A with counter = 3
    class A has 3 objects
    '''


    a_one = A()
    a_two = A()
    a_three = A()

    A.children()



if __name__ == '__main__':

    test_bench()