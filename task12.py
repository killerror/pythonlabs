from math import sqrt

S = int(input("enter S: "))
P = int(input("enter P: "))

D = S * S - 4 * P
if (D < 0):
    print("no solution")
    quit()

X = int((S + sqrt(D)) / 2)
Y = int((S - sqrt(D)) / 2)

print("X =", X)
print("Y =", Y)
