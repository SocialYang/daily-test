
def recursiveAdd(num):
    if num >1:
        result = num+recursiveAdd(num-1)
        print(result)
    else:
        result=1
    return result
result = recursiveAdd(10)
print(result)
