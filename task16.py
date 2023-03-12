import random
n = int(input("enter elements amount: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)
x = int(input("what are we looking for?: "))
count = 0
for i in lst:
    if i == x:
        count += 1
print(f"we found {x}: {count} times")
