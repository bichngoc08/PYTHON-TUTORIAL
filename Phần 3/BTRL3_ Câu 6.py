"""
 Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
"""
month = int(input("Nhập tháng: "))

if month in {1, 2, 3}:
    print("Tháng {} thuộc quý 1".format(month))
elif month in {4, 5, 6}:
    print("Tháng {} thuộc quý 2".format(month))
elif month in {7, 8, 9}:
    print("Tháng {} thuộc quý 3".format(month))
else:
    print("Tháng {} thuộc quý 4".format(month))
