from random import randint

def init_parties(parties: [str]) -> [[int]]:
    return [[0]*len(parties) for i in range(92)]

def update_election(election: [[int]], district: int, votes: [int]) -> [[int]]:
    for i in range(len(votes)):
        election[district][i] += votes[i]
    return election

def print_lead_p(election: [[int]], parties: [str]):
    total_votes = [0]*len(parties)

    for i in range(len(election)):
        for j in range(len(parties)):
            total_votes[j] += election[i][j]
    most_votes = max(total_votes)
    party_index = total_votes.index(most_votes)
    party = parties[party_index]
    print("{} is leading the election with {} votes".format(party, most_votes))

def print_results(election: [[int]], parties: [str]):
    no_votes = 0
    tied = 0
    delegates = [0]*len(parties)
    for district in election:
        sd = sorted(district)[::-1]
        if sum(sd) == 0:
            no_votes += 1
        elif sd[0] == sd[1]:
            tied += 1
        else:
            index = district.index(sd[0])
            delegates[index] += 1

    parties.extend(["Undecided (tied)", "Undecided (no votes)"])
    delegates.extend([tied, no_votes])
    longest_name = max(map(len, parties))

    for i in range(len(parties)):
        d_string = "{} delegate".format(delegates[i])
        if delegates[i] == 1:
            d_string += " "
        else:
            d_string += "s"
        print(parties[i].ljust(longest_name), d_string.rjust(14), sep="\t")

def generate_election_data(election: [[int]], parties: [str]) -> [[int]]:
    for i in range(len(election)):
        election = update_election(election, i, [randint(0, 999) for i in parties])
    return election


def main():
    print("\nTask 3a:")
    parties = ['TeaParty', 'CoffeeParty', 'MilkParty', 'HouseParty', 'BeachParty']
    election = init_parties(parties)
    print(election[:3])

    print("\nTask 3b:")
    election = update_election(election, 34, [123, 3321, 3442, 23, 1])
    print(election[34])
    election = update_election(election, 34, [601, 2000, 3000, 50, 22])
    print(election[34])

    print("\nGenerating random election data!")
    election = generate_election_data(election, parties)

    print("\nTask 3c:")
    print_lead_p(election, parties)

    print("\nTask 3d:")
    print_results(election, parties)

if __name__ == "__main__":
    main()
