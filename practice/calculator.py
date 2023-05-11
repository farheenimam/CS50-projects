n = int(input("Number: "))
m = int(input("Number: "))

print("1 = +, 2 = -, 3 = /, 4 = *")

while True:
    o = int(input("choose your operator: "))
    if o < 0 and o > 4:
        break

    if (o == 1):
        print(f"{m} + {n} = {m + n})")
    if (o == 2):
        print(f"{n} - {m} = {n - m}")
    if (o == 3):
        print(f"{n}/{m} = {n/m}")
    else:
        print(f"{n}*{m} = {n * m}")
    break