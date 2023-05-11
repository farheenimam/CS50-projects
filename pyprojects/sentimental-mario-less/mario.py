from cs50 import get_int

# For input
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break
# For rows
for i in range(0, n, 1):
    for s in range(0, n-i-1, 1):
        print(" ", end="")
    # For column
    for j in range(0, n, 1):
        if j <= i:
            print("#", end="")
    print()