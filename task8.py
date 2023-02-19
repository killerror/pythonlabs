n = int(input("enter side `n` length: "))
m = int(input("enter side `m` length: "))
k = int(input("enter `k` value: "))
print(("no", "yes")[(k % n == 0 or k % m == 0) and k < n * m])
