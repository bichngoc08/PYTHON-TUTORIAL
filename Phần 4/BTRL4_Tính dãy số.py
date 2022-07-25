# Tính S(x,n)= x + x^2/2! + x^3/3! +  ... + x^n/n!

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0


def TinhGiaiThua(a):
    giaithua = 1
    if a == 0 or a == 1:
        return giaithua
    else:
        for j in range(2, a+1, 1):
            giaithua = giaithua * j
        return giaithua


for i in range(1, n + 1, 1):
    s = s + (x ** i) / TinhGiaiThua(i)
print("S({0},{1})= {2}".format(x, n, s))
