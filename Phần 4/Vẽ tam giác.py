n = int(input("Nhập cạnh: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == j or i == n-1:
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()
