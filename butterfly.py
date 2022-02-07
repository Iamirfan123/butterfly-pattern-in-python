n=int(input("rows:"))
for i in range(0, n):
    print("*"*i, end="")
    print(" "*((n-i)*2-1), end="")
    print("*"*i)

print("*"*((2*n)-1))

for i in range(n-1,0,-1):
    print("*"*(i), end="")
    print(" "*((n-i)*2-1), end="")
    print("*"*i)
