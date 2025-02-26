"2025-2-22第17讲"
b = 1

while b <= 9:
    a = 9
    while a >= b:
        print(a,"*",b,"=",a*b,end=" ")
        a -= 1
    print()
    b += 1
