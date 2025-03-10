#2025-3-10第23讲#
import random #导入随机数模块
y = []
for a in range(88):
    y.append([])
    for b in range(88):
        y[a].append(random.randint(0,1024))
        
x = int(input('请输入一个待匹配的整数：'))
for a in range(88):
    for b in range(88):
        if y[a][b] == x:
            print(a,b)
        