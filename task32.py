import random
n = int(input("enter array elements count: "))
min = int(input("enter segment minimum: "))
max = int(input("enter segment maximum: "))

lst = [random.randrange(30) for _ in range(n)]
print(lst)
for i in range(n):
    if min <= lst[i] <= max:
        print(i, end=" ")
