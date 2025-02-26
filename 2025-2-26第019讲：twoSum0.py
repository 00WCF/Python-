"2025-2-26第19讲题目"
import random

nums = []

for a in range(10000):
    x = random.randint(1,65535)
    nums.append(x)

target = int(input("请录入目标整数："))

isFind = False
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
            isFind = True

if isFind == False:
    print("找不到！")
