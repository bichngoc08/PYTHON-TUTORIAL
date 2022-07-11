# Nhập vào 1 số bất kỳ. Trả về kết quả chẵn hay lẻ, được lặp lại liên tục.

while True:
    x = int(input('Nhập vào 1 số bất kỳ: '))
    """  if x % 2 == 0:
            print('Số chẵn')
        else:
            print('Số lẻ') """
    print(x, "là số chẵn" if x % 2 == 0 else "là số lẻ")
    s = input('Tiếp tục chương trình (c/k)')
    if s == 'k':
        break

