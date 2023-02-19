ticket = input("enter 6-digit number of ticket: ")
status = ("unlucky", "lucky")[
    sum([int(ticket[0]), int(ticket[1]), int(ticket[2])]) ==
    sum([int(ticket[3]), int(ticket[4]), int(ticket[5])])
]
print(f"your ticket is {status}")
