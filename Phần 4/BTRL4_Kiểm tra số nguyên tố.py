""" Viết chương trình nhập vào 1 số, kiểm tra số này có phải là số nguyên tố hay không. Hỏi người dùng có tiếp tục
sử dụng hay thoát phần mềm.
"""

while True:
    n = int(input("Nhập vào 1 số: "))
    count = 0
    if n == 0 or n == 1:
        print("{0} không phải là số nguyên tố".format(n))
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        else:
            continue
    if count == 2:
        print("{0} là số nguyên tố".format(n))
    else:
        print("{0} không là số nguyên tố".format(n))

    a = input("Bạn có muốn tiếp tục sử dụng phần mềm không ? (c/k): ")
    if a == 'k':
        break

