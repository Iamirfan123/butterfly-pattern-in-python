n = int(input("Enter the number of rows: "))

for i in range(n-1):
    for j in range(i):
        print(end=" ")

    for j in range( n-i):

        print("* ", end='')
    print()
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ", end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()