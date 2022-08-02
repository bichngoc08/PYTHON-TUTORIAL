"""
Nhập vào điểm toán lý hóa bằng chuỗi, theo thứ tự:
    Toán, lý, hóa -> "7,4,6"
Tính điểm trung bình lấy 2 chữ số lẻ thập phân.
"""

t, l, h, v, a, s = eval(input("Nhập điểm toán, lý, hóa, văn, anh, sinh: "))
print("Toán=", t, "Lý=", l, "Hóa=", h, "Văn=", v, "Anh=", a, "Sinh=", s)
dtb = (t+l+h+v+a+s)/6
print("Điểm trung bình =", round(dtb, 2))
