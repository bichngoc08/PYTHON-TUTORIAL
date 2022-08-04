# Nhập tọa độ A(x1,y1), B(x2,y2). Tính và xuất độ dài AB.
from math import sqrt

x1, y1 = eval(input("Nhập tọa độ A(x1,y1): "))
x2, y2 = eval(input("Nhập tọa độ B(x2,y2): "))
AB = sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
print("Độ dài đoạn AB là:", AB)
