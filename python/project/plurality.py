from cs50 import get_int, get_string
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: plurality.py [canddidate...]")

candidate = {
    "name": "alice", "votes": 0
}
# For votes
votes = get_int(" Numbers of votes: ")
for row in range(0, votes, 1):
    name = get_string("Vote: ")
    name["name"] = str(name["name"])
    names[name] +=1