# Tính tổng các số lẻ từ 1-> 15, ngoại trừ số 3 và 11.

s = 0
for i in range(1, 16, 2):
    if i == 3 or i == 11:
        continue
    s = s + i
print(s)
