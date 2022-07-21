# Nhập a là số chẵn thì tính ra sum, còn số lẻ không ra sum.

a = int(input("Nhập a: "))
s = 0
for n in range(5, 10):
    if a % 2 != 0:
        print("Nhập lại số chẵn")
        break
    s = s + n
else:
    print("Tổng = ", s)
