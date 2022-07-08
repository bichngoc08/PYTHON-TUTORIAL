# Giải phương trình bậc 2.
import math

print("Chương trình giải phương trình bậc 2")
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
delta = (b**2)-4*a*c
if a == 0:
    if b == 0 and c == 0:
        print("Phương trình vô số nghiệm")
    elif b == 0 and c != 0:
        print("Phương trình vô nghiệm")
    else:
        x = (-c)/b
        print("Phương trình có nghiệm: x =", x)
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt", x1, "và", x2)
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép:", x)
    elif delta < 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")
