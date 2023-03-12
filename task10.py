import random
n = int(input("enter coins amount: "))
headsCount = random.randrange(1, n)
tailsCount = n - headsCount
print("heads count:", headsCount)
print("tails count:", tailsCount)
print("you need to flip over", (headsCount, tailsCount)[tailsCount < headsCount], "coins")
