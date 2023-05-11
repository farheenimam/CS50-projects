from cs50 import get_string

k = get_string("Do you agree?: ")

# Over here instead of "||"  like we did in C we will use "or"
if k == 'Y' or k == 'y':
    print("agreed")
elif k == 'N' or k == 'n':
    print("not agreed")
