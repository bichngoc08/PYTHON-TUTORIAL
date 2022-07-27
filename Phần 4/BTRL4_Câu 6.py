
""" Vẽ hình vuông. """

n = int(input("Nhập cạnh: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n-1 or j == 0:
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()
print("-"*100)

""" Vẽ tam gíác vuông đều bên phải. """
for i in range(n):
    for j in range(n):
        if j == n-1 or i == n-1 or j == n-1-i:
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()
print("-"*100)

""" Vẽ 2 tam giác đối xứng. """
for i in range(2*n):
    for j in range(2*n):
        if (j == 0 and i > n-1) or (j == (2*n)-1 and i < n-1):
            print(" ", end='\t')
        elif j == 0 or j == (2*n)-1 or i == n-1 or i == j:
            print("*", end='\t')
        else:
            print(" ", end='\t')
    print()
