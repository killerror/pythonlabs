import random
n = int(input("enter first array elements amount: "))
lst_1 = [random.randrange(20) for _ in range(n)]
print(lst_1)
m = int(input("enter second array elements amount: "))
lst_2 = [random.randrange(20) for _ in range(m)]
print(lst_2)

i = [*set(lst_1).intersection(set(lst_2))]
i.sort()
print(i)
