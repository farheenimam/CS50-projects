# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Read teams into memory from file
    filename = sys.argv[1]
    with open(filename) as file:
        reader = csv.DictReader(file)
        for team in reader:
            # Square bracket to access the value for the particular key inside of a dictionary
            team["rating"] = int(team["rating"])
            teams.append(team)

    counts = {}
    # Simulate N tournaments and keep track of win counts
    for i in range(N):
        # Declaring a variable to save the results
        winner = simulate_tournament(teams)
        # To keep tarck how many times each team has won the tournament
        if winner in counts:
            # If the winner is already in the dictionary of counts
            counts[winner] += 1
            # If there are not in the dictionary of count
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # To get one winner in th end
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]["team"]


if __name__ == "__main__":
    main()
