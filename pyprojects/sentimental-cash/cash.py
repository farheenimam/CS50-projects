# To make cash in python
from cs50 import get_float

# For input
while True:
    dollar = get_float("Change owed: ")
    if dollar >= 0:
        # To convert in cents
        cents = int(dollar * 100)
        break

coins = 0
# For quaters
while cents >= 25:
    cents = cents - 25
    coins += 1
# For dimes
while cents >= 10:
    cents = cents - 10
    coins += 1
# For nikles
while cents >= 5:
    cents = cents - 5
    coins += 1
# For pennies
while cents >= 1:
    cents = cents - 1
    coins += 1

# For output
print(coins)