import csv
from cs50 import get_string

name = get_string("Name: ")
number = get_string("Number: ")

# Here 'a' stands for append which is in contrast with read and write format
# csv stands for "comma separated values
with open("phonebook.csv", "a")as file:

    writer = csv.writer(file)
    writer.writerow([name, number])