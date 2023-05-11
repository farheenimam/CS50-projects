import sys

names = ["Jeffry", "Kyle", "Ron", "Suzan", "Callisto", "Jane"]

if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)