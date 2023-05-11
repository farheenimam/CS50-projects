# Using regular expression library so it can perform search algorithm
import csv

problem = input("problem: ").strip().upper()

counter = 0

with open("lang.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # We use strip to remove white spaces
        if row ["problem"].strip().upper() == problem:
           counter += 1

print (counter)