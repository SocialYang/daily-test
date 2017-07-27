a = raw_input('Please input num_1:')
a = int(a)
b = raw_input('Please input num_2:')
b = int(b)
c = raw_input('Please input num_3:')
c = int(c)
def sum3Number(a,b,c):
    return a+b+c
def average3Number(a,b,c):
    return sum3Number(a,b,c)/3
print('sum3Number=%d'%sum3Number(a,b,c))
print('average3Number=%d'%average3Number(a,b,c))
