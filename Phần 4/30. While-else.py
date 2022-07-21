"""
Nhập một số dương bất kỳ. Nếu nhỏ hơn 5 thì tính trung bình. Lớn hơn 5 thì sai quy tắc -> kết thúc.
"""

summ = count = 0
print("Nhập danh sách 5 số dương để tính trung bình ")
while count < 5:
    val = int(input("Nhập số: "))
    if val < 0:
        print("Sai quy tắc, vui lòng nhập lại! ")
        break
    count += 1
    summ += val
else:
    print("Trung bình là:", summ/count)
