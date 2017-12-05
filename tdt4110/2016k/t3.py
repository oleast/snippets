"""
Functions for task 3 of the 2016 - Kont exam from NTNU
"""

from math import floor
from random import shuffle

#BARN =  ['Ada', 'Bo', 'Eli', 'Isa', 'Cindy', 'Henrik', 'Ine', 'Jo', 'Kim', 'Lucas', 'My', 'Noor', 'Ola', 'Pia']
BARN = ['Pia', 'Bo', 'Ada', 'Lucas', 'Emma A.', 'Cindy', 'Emma B.', 'Yngve', 'Ola', 'My', 'Quentin', 'Sara', 'Noor', 'Kim', 'Tuva', 'Rashad', 'Ine', 'Jo', 'Henrik']


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

def read_in_unmet() -> str:
    """
    Task 3c (4%)
    """
    unmet = []
    print("Skriv navn, eller kun ENTER (tom tekst) for å avslutte.")
    while True:
        name = input("Spiller som har meldt forfall: ")
        if name != "":
            unmet.append(name)
        else:
            break
    return unmet

def find_available(players: list, unmet: list) -> list:
    """
    Task 3d (4%)
    """
    #return [p for p in players if p not in unmet]
    return list(set(players) - set(unmet))

def team_placement(players: list, team_size: int) -> list:
    """
    Task 3e (6%)
    """
    random_players = players
    shuffle(random_players)
    team_list = []
    for i in range(floor(len(players) / team_size)):
        team_list.append(random_players[0:team_size])
        random_players = random_players[team_size:]
    for i, player in enumerate(random_players):
        team_index = i%3
        team_list[team_index].append(player)
    return team_list

def new_file(team_name: str, input_filename: str, output_filename: str):
    input_file = open(input_filename)
    games = input_file.read().split("\n")
    input_file.close()

    filtered_games = list(filter(lambda game: team_name in game, games))

    output_file = open(output_filename, "w")
    output_file.write("\n".join(filtered_games))
    output_file.close()

def main():
    """
    Task 3f (5%)
    """
    unmet = read_in_unmet()
    num_team_active = int(input("Spillere per lag: "))
    game_time = int(input("Kamptid (minutter): "))
    team_name = input("Navn på laget: ")

    available = find_available(BARN, unmet)
    teams = team_placement(available, num_team_active)
    for i, team in enumerate(teams):
        bench_time = sec_on_bench(len(team), num_team_active, game_time)
        print("Lag {} :\n{}\nTid på Benken per spiller: {}".format(i, team, min_to_sec(bench_time)))

    new_file(team_name, "input-games.txt", "output-games.txt")


if __name__ == "__main__":
    main()