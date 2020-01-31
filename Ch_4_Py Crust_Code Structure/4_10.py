
def test(func):
    

    def new_function(*args, **kwargs):
        
        print('start')
        result = func(*args, **kwargs)
        print('end')    
        

        return result

    return new_function



@test
def adder(a, b):
    print( f"function return is : {a+b}"  )
    return a+b



# expected output:
'''
start
function return is : 8
end
'''
x = adder(3,5) 