# Xuất bảng cửu chương từ 2 đến 9.

for i in range(1, 11):
    for j in range(2, 10):
        line = "{0}* {1:>2} ={2:>2}".format(j, i, j * i)
        print(line, end='\t')  # Thụt đầu dòng
    print()  # để xuống dòng chạy vòng lặp tiếp theo sau khi kết thúc một hàng với tất cả các cột
