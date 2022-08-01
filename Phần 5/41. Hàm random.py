# Xuất giá trị ngẫu nhiên đến khi có giá trị là 50 thì dừng lại.
import random

count = 0
while True:
    x = random.randint(1, 100)
    print(x)
    count += 1
    if x == 50:
        break
print("count= ", count)
