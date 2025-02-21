import random

counts = int(input("请输入抛硬币的次数："))
i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
print("开始抛硬币实验：")
while counts != i:
    if counts < 100:
        while i < counts:
            num = random.randint(1, 10)

            if num % 2:
                print("正面", end=" ")
                d = 0
                a = a+1
                c = c+1
                if c > e:
                    e = e+1
            else:
                print("反面", end=" ")
                c = 0
                b = b+1
                d = d+1
                if d > f:
                    f = f+1

            i += 1
    else:
        while i < counts:
            num = random.randint(1, 10)

            if num % 2:
                d = 0
                a = a+1
                c = c+1
                if c > e:
                    e = e+1
            else:
                c = 0
                b = b+1
                d = d+1
                if d > f:
                    f = f+1

            i += 1
print("")
print("一共模拟了",counts,"次抛硬币，结果如下：")
print("正面：",a,"次")
print("反面：",b,"次")
print("最多连续正面：",e,"次")
print("最多连续反面：",f,"次")
