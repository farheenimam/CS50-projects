from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for row in range(0, n, 1):
    for space in range(0, n, 1):
        if space < n-row-1:
            print("  ")
        for column in range(0, n, 1):
            if column <= row:
                print("#", end="")
            print()