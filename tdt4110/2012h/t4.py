
from random import randint

"""
Oppgave 4 – Programmering (40 %)
Denne oppgaven fokuserer på behandling av data fra fire værsensorer som måler en verdi per
døgn av følgende data:
• Temperatur: Angis som heltall i Celsius fra -50 C til + 50 C
• Nedbør: Angis som heltall i mm nedbør per døgn fra 0 til 2000 mm
• Luftfuktighet. Angis som heltall fra 0 til 100 %
• Vindstyrke: Angis som heltall fra 0 til 50 meter per sekund
Hvis ikke noe annet er oppgitt kan du anta korrekt input til funksjonene.
"""

"""
Oppgave 4 a) (5 %)
Lag en funksjon cold_days som tar imot parameteren templist, som en liste av
temperaturer, og returnerer variabelen days, som angir antall døgn der temperaturen var
under 0 grader.
"""
def cold_days(templist: list) -> int:
    """
    Funksjonen finner antallet antallet elementer i listen som er under '0'.
    """
    days = 0
    for temp in templist:
        if temp < 0:
            days += 1
    return days

"""
Oppgave 4 b) (5 %)
Lag en funksjon cap_data som har inn-parameterne array (liste med data), min_value
(minimumsverdi) og max_value (maksimumsverdi). Funksjonen skal returnere ei ny liste
result der alle elementer i lista array som har verdi mindre enn min_value skal settes
lik min_value og alle elementer i lista array som har verdi høyere enn max_value skal
settes lik max_value. 
"""
def cap_data(array: list, min_value: int, max_value: int) -> list:
    """
    Funksjonen setter en maks, og min verdi på alle elementer i en liste.
    """
    fixed = []
    for data in array:
        if data < min_value:
            fixed.append(min_value)
        elif data > max_value:
            fixed.append(max_value)
        else:
            fixed.append(data)
    return fixed

"""
Oppgave	4 c) (10 %)
Lag en funksjon generate_testdata som har inn-parameterne N, min_value
(minimumsverdi) og max_value (maksimumsverdi). Funksjonen skal returnere tabellen
result som består av N unike tall (heltall) som blir trukket tilfeldig der
{min_value ≤ tall ≤ max_value}. Unik betyr her at ingen elementer i tabellen
result skal ha samme verdi. Du kan anta at antall mulige verdier i intervallet tallet blir
trukket fra alltid vil være større enn N.
"""
def generate_testdata(N: int, min_value: int, max_value: int) -> list:
    """
    Returnerer en liste av lengde 'N' med tildeldige tall mellom 'min_value' og 'max_value'.
    """
    numbers = set([])
    while len(numbers) < N:
        random = randint(min_value, max_value)
        numbers.add(random)
    return list(numbers)

"""
Oppgave	4 d) (5 %)
Lag en funksjon create_db som har inn-parameterne temp, rain, humidity og wind,
som er fire tabeller av samme størrelse (likt antall elementer) med data for temperatur,
nedbør, luftfuktighet og vind.
Funksjonen skal lage og returnere dictionarien weather, der nøkkelen er ett heltall som
starter med verdien 1 og teller oppover (representerer dagen for måling). Hvert innslag i
dictionarien skal være en liste av verdier for temperatur, nedbør, luftfuktighet og vind.
Verdiene for weather med nøkkel 1 skal inneholde væredata for dag 1, weather med
nøkkel 2 skal inneholde værdata for dag 2 og så videre.
Eksempel på kall av funksjonen og hva den returnerer:
"""
def create_db(temp: list, rain: list, humidity: list, wind: list) -> dict:
    """
    Restrukturerer fire lister til en dictionary med en list med en verdi fra hver input liste.
    """
    weather = {}
    for i in range(len(temp)):
        weather[i+1] = [temp[i], rain[i], humidity[i], wind[i]]
    return weather

"""
Oppgave 4 e) (5 %)
Lag en funksjon print_db som har inn-parameteren weather, som er en dictionary som
beskrevet i oppgave 4d. Funksjonen skal skrive ut innholdet i weather på skjerm etter
følgende format og med overskrift som vist på utskriften nederst i deloppgaven:
• Day (dag) – høyrejustert med 4 tegn
• Temp (temperatur) – høyrejustert med 6 tegn
• Rain (nedbør) – høyrejustert med 6 tegn
• Humidity (luftfuktighet) – høyrejustert med 10 tegn
• Wind (vind) – høyrejustert med 6 tegn
"""
def print_db(weather: dict):
    """
    Printer ut en fancy tabell for å representere data.
    """
    print("Day | Temp | rain | humidity | wind ")
    print("====+======+======+==========+======")
    for i in range(1, len(weather) + 1, 1):
        day = weather[i]
        print(format(i, "4d"), format(day[0], "6d"), format(day[1], "6d"), format(day[3], "10d"), format(day[3], "6d"))


"""
Oppgave 4 f) (10 %)
Lag funksjonen strange_weather som har inn-parameterne temp og rain, som er to
tabeller med data for temperaturer og regn av lik størrelse (samme antall elementer).
Funksjonen skal returnere start (startdag) og stop (sluttdag) for det lengste intervallet der
det er minusgrader, samt at temperaturen faller samtidig som nedbørsmengden stiger i
etterfølgende dager. Indekseringen av dager starter på 1. Hvis ingen etterfølgende dager har
denne karakteristikken, returneres (0,0).
"""
def strange_weather(temp: list, rain: list) -> (int, int):
    """
    Returnerer dagene med lengst durasjon med merkelig vær.
    """
    start = 0
    chain = 0
    current_chain = 0
    for i in range(1, len(temp), 1):
        if (temp[i] < temp[i-1]) and (rain[i] > rain[i-1]):
            current_chain += 1
        else:
            if current_chain > chain:
                start = i - current_chain
                chain = current_chain
            current_chain = 0
    return start, start + chain

def main():
    """
    Testing av funksjonene jeg har laget.
    """

    print("\nTask 4a:")
    days = cold_days([1, -5, 3, 0, -6, -3, 15, 0])
    print(days)

    print("\nTask 4b:")
    A = [-70, 30, 0, 90, 23, -12, 95, 12]
    result = cap_data(A, -50, 50)
    print(result)

    print("\nTask 4c:")
    for i in range(4):
        print(generate_testdata(10, -5, 10))

    print("\nTask 4d:")
    temp = [1, 5, 3]
    rain = [0, 30, 120]
    humidity = [30, 50, 65]
    wind = [3, 5, 7]
    weather = create_db(temp, rain, humidity, wind)
    print(weather)

    print("\nTask 4e:")
    print_db(weather)

    print("\nTask 4f:")
    temp = [1, 3, 4, -5, -6, -7, -8, -9, 3, 0]
    rain = [0, 20, 30, 0, 10, 30, 50, 0, 5, 2]
    print(strange_weather(temp, rain))

if __name__ == "__main__":
    main()
