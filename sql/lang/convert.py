# Python program to convert tsv file into cv file
import re

# Reading given tsv file
with open("lang.tsv", 'r') as file:
    with open("lang.csv", 'w') as csvfile:
        for line in file:

            # Replace every tab with comma
            filecontent = re.sub("\t", ",", line)

            # Writing into csv file
            csvfile.write(filecontent)

# Output
print("Successfully made csv file")