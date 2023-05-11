from cs50 import get_string

k = get_string("Do you agree? ").lower()
if k in ["y", "yes"]:
    print("agreed")
if k in ["n", "no"]:
    print("not agreed")