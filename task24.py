import random
n = int(input("enter shrubs count on the line: "))
lst = [random.randrange(10) for _ in range(n)]
print(lst)

maxHarvest = 0
for i in range(n):
    if (i == (n-1)):
        harvest = lst[i-1]+lst[i]+lst[0]
    else:
        harvest = lst[i-1]+lst[i]+lst[i+1]
    if harvest > maxHarvest:
        maxHarvest = harvest
print(f"maximum harvest: {maxHarvest}")
