
print("Nhập 1 số: ")
n = int(input())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
    if count == 2:
        print("{0} là số nguyên tố".format(n))
    else:
        print("{0} không phải số nguyên tố".format(n))
    print("Tiếp không (c/k)?")
    if input() == "k":
        exit()
print("BYE")
