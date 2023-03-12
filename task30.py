a1 = int(input("enter first element of progression: "))
d = int(input("enter difference: "))
n = int(input("enter element count: "))
lst = [a1]
for i in range(2, n+1):
    ai = a1+(i-1)*d
    lst.append(ai)
print(*lst)
