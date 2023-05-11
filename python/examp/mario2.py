from cs50 import get_int

# For input
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break
# For rows
for row in range(0, n, 1):
    # For column
    for column in range(0, n, 1):
        if column <= row:
            print("#", end="")
    print()

