"""
 Nhập vào 2 giá trị a,b và phép toán '+', '-', '*', '/'. Hãy xuất kết quả theo đúng phép toán đã nhập.
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
t = input("Nhập phép toán: ")

if t == "+":
    z = a + b
    print("Kết quả là:", z)
elif t == "-":
    z = a - b
    print("Kết quả là:", z)
elif t == "*":
    z = a * b
    print("Kết quả là:", z)
elif t == "/":
    z = a / b
    print("Kết quả là:", z)
else:
    print("Phép toán không hợp lệ!")
