n = int(input("请输入一个正整数："))

while n > 0:
    if n%2==0:
        print(n,"/","2"," = ",int(n/2), sep="")
        y = int(n/2)
        n = y
    else:
        print(n,"*","3","+","1"," = ",int(n*3+1),sep="")
        y = int(n*3+1) 
        n = y
    if n == 1:
       break

