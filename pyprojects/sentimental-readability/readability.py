# To make readability in python
from cs50 import get_string

# For text
text = get_string("Text: ")

# To count number of words, letters and sentences
letters = 0
words = 1
sentences = 0

# For numbers of letters
for i in range(0, len(text), 1):
    if (text[i].isalpha()) == True:
        letters += 1
    # For numbers of words
    if (text[i].isspace()) == True:
        words += 1
    # For numbers of sentences
    if text[i] == '.' or text[i] == '?' or text[i] == '!':
        sentences += 1

# To calculate the text
Lett = letters / words * 100
Sent = sentences / words * 100

# Convert into float
L = float(Lett)
S = float(Sent)

index = round(0.0588 * L - 0.296 * S - 15.8)

# To print the Grade no. of the text
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
