"""
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra điểm trung bình của học sinh đó
với hai số lẻ thập phân.
"""
t = float(input("Nhập điểm toán: "))
l = float(input("Nhập điểm lý: "))
h = float(input("Nhập điểm hóa: "))
dtb = (t + l + h) / 3
print("Điểm trung bình là: ", dtb)
print("Điểm trung bình là:", round(dtb, 2))
