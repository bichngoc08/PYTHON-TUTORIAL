# Nhập 1 số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
# (Ví dụ: n = 35 -> Ba mươi lăm, n = 5 -> năm).

import re

print("Nhập số n có tối đa 2 chữ số: ")
n = input()
t = re.findall(r'\d', n) # Hàm tách số thành 1 list
# Dãy array dò chỉ số theo trật tự được thiết lập từ trước
numbers = {0: "Không", 1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín",
           10: "mười", "00": "mươi"}
a = int(n)
if a <= 10:
    print("{}".format(numbers[a]))
elif a <= 19:
    print("{} {}".format(numbers[10], numbers[int(t.pop(-1))]))
elif a in {20, 30, 40, 50, 60, 70, 80, 90}:
    print("{} {}" .format(numbers[int(t.pop(-2))], numbers["00"]))
else:
    print("{} {} {}" .format(numbers[int(t.pop(-2))], numbers["00"], numbers[int(t.pop(-1))]))
