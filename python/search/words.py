import sys

words = {"apple", "banana", "pinneapple", "watermelon", "pumpkin", "pear", "strawberry"}

if "watermelon" in words:
    print("Found")
    sys.exit(0)

print("not found")
sys.exit(1)