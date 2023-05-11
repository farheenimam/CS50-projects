from cs50 import get_int

# For input
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

# For rows
for i in range(0, n, 1):
    # For spaces
    for s in range(0, n-i-1, 1):
        print(" ", end="")
    # For columns
    for j in range(0, n, 1):
        if j <= i:
            print("#", end="")
    print("  ", end="")
    for j in range(0, n, 1):
        if j <= i:
            print("#", end="")
    print()