# Nhập vào một số. Nếu số đó là số lẻ thì cộng dồn các số lẻ, số chẵn thì cộng dồn các số chẵn.

n = int(input('Nhập vào một số tự nhiên bất kỳ: '))
s = 0
if n % 2 == 0:
    for i in range(0, n+1, 2):
        s += i
else:
    for i in range(1, n+1, 2):
        s += i
print(s)
