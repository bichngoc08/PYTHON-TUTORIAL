# Vẽ chữ N có chiều cao là k bất kỳ.

k = int(input("Nhập chiều cao: "))
for i in range(k): # i là hàng, j là cột
    for j in range(k): # Kết thúc hết vòng for bên trong là hết các cột và hết 1 dòng
        if j == 0 or i == j or j == k-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
print("-"*30)

i = 0
while i < k:
    j = 0
    while j < k:
        if j == 0 or i == j or j == k - 1:
            print("*", end='')
        else:
            print(" ", end='')
        j += 1
    i += 1
    print()
