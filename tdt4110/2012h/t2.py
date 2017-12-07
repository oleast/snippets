from datetime import datetime

"""
Oppgave 2 – Grunnleggende programmering (20 %)
Du kan anta at alle funksjonene mottar gyldige input-verdier.
"""

"""
Ferdiggitte funksjoner på eksamen,
laget for at programmet skal kjøre i virkeligheten...
"""
def current_date():
    """
    Returnerer nåværende år, måned og dag på formatet (yyyy,mm,dd) som heltall.
    """
    now = datetime.now()
    return now.year, now.month, now.day

"""
Oppgave 2 a) (5 %)
Lag funksjonen summerOlympics som har inn-parametere firstYear og lastYear.
Funksjonen skal returnere variabelen years, som er ei liste med alle OL-årene fra og med
firstYear til og med lastYear (inkludert framtidige planlagte år for sommer-OL). Fra
og med OL i London i 1948, har sommer-OL vært arrangert hvert fjerde år.
Du kan anta at firstYear ≥ 1948
"""
def summer_olympics(first_year: int, last_year: int) -> list:
    """
    Returnerer en liste med hvert fjerde år mellom 'first_year' og 'last_year'.
    """
    years = []
    actual_first_year = first_year + (4 - (first_year % 4))
    for year in range(actual_first_year, last_year + 1, 4):
        years.append(year)
    return years

"""
Oppgave 2 b) (7,5 %)
Lag funksjonen findAge som har inn-parametere bYear, bMonth, bDay som er tre heltall
som beskriver dato for en fødselsdag. Funksjonen skal returnere age som beskriver hvor
gammel en person med oppgitt fødselsdag (bYear, bMonth og bDay) er i dag angitt i hele
år.
For å finne år, måned og dag for i dag skal du bruke en eksisterende funksjon som heter
current_date(). Funksjonen returnerer tre heltall på formatet (yyyy,mm,dd).
"""
def find_age(b_year: int, b_month: int, b_day: int) -> int:
    """
    Returnerer alderen på en person med gitt fødselsdato.
    """
    (year, month, day) = current_date()
    if b_month > month or (b_month == month and b_day > day):
        return (year - b_year) - 1
    else:
        return year - b_year

"""
Oppgave 2 c) (7,5 %)
Lag en funksjon printAgeDiff som tar en parameter table, som er en to-dimensjonal
tabell (liste av lister) der hver rekke beskriver personer med fornavn, etternavn, fødselsår,
fødselsmåned og fødselsdato. Funksjonen skal bruke funksjonen findAge fra oppgave 2b
(kan bruke funksjonen selv om du ikke har løst oppgave 2b) til å sammenlikne alderen i hele
år på etterfølgende personer i tabellen (rekke for rekke) og gjøre følgende:
• Hvis person n og person n+1 har samme alder angitt i antall hele år, skal følgende skrives ut til skjerm:
<fornavn n> <etternavn n> is at the same age as <fornavn n+1> <etternavn n+1>
• Hvis person n er eldre enn person n+1 angitt i antall hele år, skal følgende skrives ut til skjerm:
<fornavn n> <etternavn n> is older than <fornavn n+1> <etternavn n+1>
• Hvis person n er yngre enn person n+1 angitt i antall hele år, skal følgende skrives ut til skjerm:
<fornavn n> <etternavn n> is younger than <fornavn n+1> <etternavn n+1>
"""
TABLE = [
    ['Justin', 'Bieber', 1994, 3, 1],
    ['Donald', 'Duck', 1934, 8, 1],
    ['George', 'Clooney', 1961, 5, 6],
    ['Eddie', 'Murphy', 1961, 4, 3]
]

def print_age_diff(table: list):
    """
    Find the age of each person.
    Then prints out how that person compares to the next person in the list.
    """
    for i, person in enumerate(table):
        age = find_age(person[2], person[3], person[4])
        person.append(age)

    for i in range(len(table) - 1):
        person = table[i]
        compare = table[i+1]
        compare_string = ""

        if person[5] < compare[5]:
            compare_string = "is younger than"
        elif person[5] > compare[5]:
            compare_string = "is older than"
        else:
            compare_string = "is at the same age as"

        print("{} {} {} {} {}".format(person[0], person[1], compare_string, compare[0], compare[1]))


def main():
    """
    Testing av funksjonene jeg har laget.
    """

    print("\nTask 2a:")
    years = summer_olympics(1999, 2012)
    print(years)

    print("\nTask 2b:")
    age = find_age(2000, 12, 15)
    print(age)

    print("\nTask 2c:")
    print_age_diff(TABLE)

if __name__ == "__main__":
    main()
