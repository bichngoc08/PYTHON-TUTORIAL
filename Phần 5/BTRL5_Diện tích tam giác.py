"""
Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác. Sau đó tính diện tích theo công thức Herong.
"""
import math

a, b, c = eval(input("Nhập vào 3 cạnh a,b,c: "))
print("a=", a, "b=", b, "c=", c)
if (a <= 0 or b <= 0 or c <= 0) or (a+b) <= c or (a+c) <= b or (b+c) <= a:
    print("Tam giác không hợp lệ")
else:
    cv = a + b + c
    p = cv/2
    dt = math.sqrt(eval("p*(p-a)*(p-b)*(p-c)"))
print("cv=", cv, "p=", p, "dt=", dt)
