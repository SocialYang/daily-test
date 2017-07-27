def function_B():
    print('------function_B start------')
    print('------function_B end------')
def fuction_A():
    print('------function_A start------')
    function_B()
    print('------function_A end------')
fuction_A()
