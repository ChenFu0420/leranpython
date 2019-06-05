a = 1
for i in range(1, 10):
    for b in range(1, 10):
        if i >= b:
            print("%s X %s = %d\t" %(i, b, i * b),end=" ")
    print()