n = eval(input())
for i in range(n):
    for j in range(0, n - i):
        print(end=" ")
    for k in range(2 * i + 1):
        print("*",end="")
    print()