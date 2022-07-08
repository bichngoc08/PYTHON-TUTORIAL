# Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không.
# Biết rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400

try:
    print("Nhập vào 1 năm bất kỳ: ")
    t = int(input())
    if (t % 4 == 0 and t % 100 != 0) or t % 400 == 0:
        print("{0} là năm nhuần".format(t))
    else:
        print("{0} không phải là năm nhuần".format(t))
except:
    print("Vui lòng nhập năm là 1 số nguyên!!")
