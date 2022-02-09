n=int(input("rows:"))

for i in range(0, 2*n):
    if i < n:
        print("*" * i, end="")
        print(" " * ((n - i) * 2 - 1), end="")
        print("*" * i)
    elif i == n:
        print("*" * ((2 * n) - 1))
    else:
        print("*" * (2*n - i), end="")
        print(" " * (0-((n - i) * 2 +1)), end="")
        print("*" * (2*n - i))