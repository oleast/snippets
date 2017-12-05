"""
Functions for task 3 of the 2016 - Kont exam from NTNU
"""

from math import floor

def sec_on_bench(team_size: int, num_team_active: int, game_time: int) -> int:
    """
    Task 3a (4%)
    """
    return ((game_time / (team_size)) * (team_size - num_team_active)) * 60

def min_to_sec(seconds: int) -> str:
    """
    Task 3b (4%)
    """
    minutes = floor(seconds / 60)
    seconds = seconds % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    return "{}:{}".format(minutes, seconds)

def main():
    exit()

if __name__ == "__main__":
    main()