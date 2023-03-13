s = float(input("Mời bạn nhập giá trị:"))
print("bạn nhập", s)
print(type(s))

""" 
    1. Đặt hàm là StrToBool có a là 1 chuỗi
    2. Trả về chuỗi được viết thường 
"""


def StrToBool(a):  # Định nghĩa 1 hàm, có giá trị đầu vào là a
    return a.lower() in ("true", "t", "1", "yes")


"""
    3.  Nếu khi nhập có các từ như trên thì sẽ trả kết quả về True
"""

x = input("Mời bạn nhập True/False:")
x = StrToBool(x)  # Gọi hàm
print(x)
