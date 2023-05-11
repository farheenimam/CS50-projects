import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence")

    data = []
    # Read database file into a variable
    database = sys.argv[1]
    with open(database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        seq = file.read()

    longest = {}
    # Find longest match of each STR in DNA sequence
    subsequences = list(data[0].keys())[1:]

    for subsequence in subsequences:
        longest[subsequence] = longest_match(seq, subsequence)

    # Check database for matching profiles
    for people in data:
        check = 0
        for subsequence in subsequences:
            if int(people[subsequence]) == longest[subsequence]:
                check += 1

        # Print the result
        if check == len(subsequences):
            print(people["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()

