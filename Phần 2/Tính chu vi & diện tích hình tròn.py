import math

try:
    r = float(input("Mời bạn nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    dt = math.pi * (r ** 2)
    print("Chu vi hình tròn là:", cv)
    print("Diện tích hình tròn là:", dt)
except:
    print("Lỗi rồi! Mời bạn nhập lại.")
print("-"*20)
print("Cám ơn đã thực hiện phép tính")
