# Viết chương trình yêu cầu nhập vào một số nguyên dương [1...10], nếu nhập sai yêu cầu nhập lại.
# Khi nhập đúng thì xuất ra bình phương của giá trị mới nhập vào.

x = int(input("Nhập 1 số [1...10]: "))
while x < 1 or x > 10:
    x = int(input("Nhập [1...10]"))
print(pow(x, 2))
