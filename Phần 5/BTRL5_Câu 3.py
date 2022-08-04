"""
Viết chương trình tính logax với a,x là các số thực nhập vào từ bàn phím, và x>0, a>0, a!=1.
"""
from math import *

x = float(input("Nhập x>0: "))
a = float(input("Nhập a>0: "))
if x <= 0 or a <= 0 or a == 1:
    print("Mời bạn nhập lại! ")
else:
    #    logax = log(x, a)
    logax = log(x) / log(a)
print("logax=", logax)
