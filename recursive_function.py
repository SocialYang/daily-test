def recursiveAdd(num):
    result = 0
    if num >= 1:
        result = num+recursiveAdd(num-1)
        print(result)
    return result
result = recursiveAdd(10)
print(result)
