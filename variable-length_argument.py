def test_1(a,b,*args,**kvargs):
    print(a)
    print(b)
    print(args)
    print(kvargs)
test_1(1,2)
print('------------------------')
test_1(1,2,3,4,5)
print('------------------------')
test_1(1,2,3,4,5,m = 7,n = 8)

'''
1
2
()
{}
------------------------
1
2
(3, 4, 5)
{}
------------------------
1
2
(3, 4, 5)
{'m': 7, 'n': 8}
'''
