
"""
Oppgave 2a (5%)
"""
def yatzy(t1: int, t2: int, t3: int, t4: int, t5: int) -> list:
    dices = [t1, t2, t3, t4, t5]
    for dice in dices:
        if (dice < 1) or (dice > 6):
            return ValueError("Terningsverdi {} er ikke mellom 1 og 6!".format(dice))
    dices.sort()
    return dices

"""
Oppgave 2b (5%)
"""
def maxi_yatzy(dices: list) -> str:
    length = len(dices)
    if length == 5 or length == 6:
        values = [0 for i in range(length)]
        for dice in dices:
            values[dice-1] += 1

        largest_count = max(values)
        values.reverse()
        largest_dice = (length - values.index(largest_count))

        return "Du kastet {} terninger og fikk flest {} ({} like).".format(length, largest_dice, largest_count)
    else:
        return ValueError("Skulle kaste 5 eller 6 terninger, men kastet {}".format(length))

def main():

    print("\nTask 2a:")
    print(yatzy(1, 4, 6, 6, 1))
    print(yatzy(1, 4, 6, 4, 10))
    print(yatzy(1, 4, 6, 0, 1))

    print("\nTask2b:")
    print(maxi_yatzy([1, 2, 3, 4, 4, 3]))

if __name__ == "__main__":
    main()
