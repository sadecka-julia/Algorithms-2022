

n = int(input("Enter the number\n"))
space = n-1
stars = 1
for i in range(n):
    print(" "*space, "*"*stars, sep='')
    space -= 1
    stars += 1
