"第六讲作业"
num = input("请输入你的分数：")

while num != "e":
    num = int(num)
    if num == 100:
        print("S")
    if 100 > num >= 90:
        print("A")
    if 90 > num >= 80:
        print("B")
    if 80 > num >= 60:
        print("C")
    if 60 > num:
        print("D")
            
    num = input("请输入你的分数：")
