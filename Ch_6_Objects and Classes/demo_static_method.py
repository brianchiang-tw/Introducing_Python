
class TestClass():

    def __init__(self):
        pass

    def demo_static_method():

        print("static method does not require initialized objects to invoke.")



def test_bench():

    # expected output:
    '''
    static method does not require initialized objects to invoke.
    '''
    TestClass.demo_static_method()



if __name__ == '__main__':

    test_bench()