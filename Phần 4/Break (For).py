# Nhập vào n. Tính tổng của nó lớn hơn 15 thì dừng lại.

n = int(input("Nhập vào 1 số: "))
s = 0
for i in range(1, n+1, 1):
    s = s + i
    if s >= 15:
        break
print(s)
