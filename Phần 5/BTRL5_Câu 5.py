from time import sleep

n = int(input("Nhập số cạnh: "))
for i in range(0, 2 * n - 1):
    for j in range(0, 2 * n - 1):
        if (j == n - 1 and i <= n - 1) or (j == 0 and i >= n - 1) or i == n - 1 or (
                j <= (2 * n) - 2 - i and i >= n - 1) or (n - 1 + i >= j >= n - 1 >= i):
            print("*", end='\t')
        elif (j == n - 1 + i and i <= n - 1) or (j == (2 * n) - 2 - i and i >= n - 1):  # Đường chéo
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()

print("-" * 100)

sleep(1)
for i in range(0, 2 * n - 1):
    for j in range(0, 2 * n - 1):
        if (j == n - 1 and i <= n - 1) or (j == 0 and i >= n - 1) or i == n - 1:
            print("*", end='\t')
        elif (j == n - 1 + i and i <= n - 1) or (j == (2 * n) - 2 - i and i >= n - 1):  # Đường chéo
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()

print("-" * 100)
sleep(1)
for i in range(0, 2 * n - 1):
    for j in range(0, 2 * n - 1):
        if j == n - 1 or (i == 0 and j >= n - 1) or (i == 2 * n - 2 and j <= n - 1) or j == (2 * n) - 2 - i:
            print("*", end='\t')
        elif (i <= n - 1 <= j <= (2 * n) - 2 - i) or (i >= n - 1 and n-1 >= j >= (2 * n) - 2 - i):
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()

print("-" * 100)
sleep(1)
for i in range(0, 2 * n - 1):
    for j in range(0, 2 * n - 1):
        if j == n - 1 or (i == 0 and j >= n - 1) or (i == 2 * n - 2 and j <= n - 1) or j == (2 * n) - 2 - i:
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()
