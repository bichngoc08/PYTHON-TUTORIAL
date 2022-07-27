""" Nhập x,n. Tính:
S(x,n) = x + (x^3)/3! + (x^5)/5! + ... + (x^(2n+1))/(2n+1)!
"""

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0
for i in range(n+1):
    tu = x**(2*i+1)
    mau = 1
    for j in range(1, (2*i)+2):
        mau = mau*j
    s = s + tu/mau
print("S =", s)
