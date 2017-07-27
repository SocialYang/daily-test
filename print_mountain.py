height = raw_input("Please input the height of a mountain:")
height = int(height)
i = 1
while i<= height:
    print("*"*i)
    i += 1
    if i == height+1:
        while i >= 1:
            print("*"*(i-1))
            i -= 1
    if i == 1:
        break
