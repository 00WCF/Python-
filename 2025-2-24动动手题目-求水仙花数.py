"2025-2-24动动手题目-求水仙花数"

for i in range(100, 1000):
    sum = 0
    temp = i
   
    while temp:
        sum = sum + (temp % 10) ** 3
        temp //= 10
   
    if sum == i:
        print(i)
        
