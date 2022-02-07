n = int(input("rows:"))



for i in range(1, n):
    print(end="\t")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, (2 * (n - i)) + 1):
        print( end=" ")
    print(end="\b")
    for j in range(i, 0, -1):
        print("*", end="")
    print(end="\n")

for i in range(n, 0, -1):
    print(end="\t")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, (2 * (n - i)) + 1):
        print(end=" ")
    print(end="\b")
    for digits in range(i, 0, -1):
        print("*", end="")
    print(end="\n")