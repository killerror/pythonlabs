import random
n = int(input("enter array elements amount: "))
lst = [random.randrange(100) for _ in range(n)]
print(lst)
x = int(input("getting closer to?: "))

lst2 = []
for i in lst:
    lst2.append(abs(i-x))
print(f"closest element is {lst[lst2.index(min(lst2))]}")