#!/usr/bin/env python3

# Packers Stats Tracker
# Going back to basics to review Python fundamentals in a fun way

# Variables
packers_scores = []
opponent_scores = []
opposing_team = []

# Input game results
print("Enter the opposing team and scores for each game (Packers first, then opponents). Type 'done' to finish.")
while True:
    opponent = input("Opposing team: ")
    if opponent.lower() == "done":
        break
    packers = input("Packers score: ")
    if packers.lower() == "done":
        break
    opponents = input("Opponent score: ")
    if opponents.lower() == "done":
        break

    # Add scores to lists
    opposing_team.append(str(opponent))
    packers_scores.append(int(packers))
    opponent_scores.append(int(opponents))

# Calculate stats
total_games = len(packers_scores)
if total_games > 0:
    total_points = sum(packers_scores)
    average_points = total_points / total_games
    wins = sum(1 for p, o in zip(packers_scores, opponent_scores) if p > o)
    win_percentage = (wins / total_games) * 100

    # Print summary
    print("\n--- Packers Season Stats ---")
    print(f"Total Games: {total_games}")
    print(f"Total Points Scored: {total_points}")
    print(f"Average Points per Game: {average_points:.2f}")
    print(f"Total Wins: {wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")
else:
    print("No games entered. Go Pack Go!")
