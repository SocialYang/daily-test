sum = lambda a,b:a+b
print(sum(2,4))

def test(a,b):
    return lambda a,b :a+b
print(test(1,2)(3,4))

def test_1(a,b,c):
    print('a=%d'%a)
    print('b=%d'%b)
    print('c=%d'%c(a,b))
test_1(3,5,lambda a,b:a+b)

a = lambda x,y:lambda z:x+y+z
print(a(3,5)(7))
