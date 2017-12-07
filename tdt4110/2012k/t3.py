"""
Oppgave 3 – Grunnleggende programmering (20 %)
Skøyteløp arrangeres på en rundbane som er 400 m. Et løp på 1500 m består for eksempel av
300 m pluss tre hele runder. For hver passering av målstreken tar man en passeringstid, den
siste målpasseringen er resultatet i løpet.
Det er hensiktsmessig å bruke funksjonene du lager utover i oppgaven. Du kan bruke
funksjoner fra andre deloppgaver selv om du ikke har klart å løse deloppgaven der du skal
lage funksjonen. Du kan forutsette at alle inndata er riktige.
"""

"""
Oppgave 3 a) (5 %)
Lag funksjonen mshd2s(minutter, sekunder, hundredeler) som konverterer
tid i minutter, sekunder og hundredeler til sekunder.
"""
def mshd2s(minutes: int, seconds: int, hundredths: int) -> float:
    """
    Tar minutter, sekunder og hundredeler og gjør det om til sekunder.
    """
    return (minutes * 60) + seconds + (hundredths / 100)

"""
Oppgave 3 b) (5 %)
Rundetiden er tiden mellom to målpasseringer. Lag funksjonen rundeTid(startTid,
sluttTid) som regner ut rundetiden (i sekunder med desimaler) når startTid og sluttTid er
lister med minutter, sekunder og hundredeler.
"""
def lap_time(start_time: list, end_time: list) -> float:
    """
    Tar tidsstempler på '[minutter, sekunder og hundredeler]' og returnerer differansen.
    """
    start = mshd2s(start_time[0], start_time[1], start_time[2])
    end = mshd2s(end_time[0], end_time[1], end_time[2])
    return end - start

"""
Oppgave 3 c) (10 %)
Lag funksjonen alleRundeTider(passeringsTider) som returnerer en liste med
alle rundetider (sekunder med desimaler) for et skøyteløp. Parameteren passeringsTider
er en liste av lister med alle passeringstider, der hver delliste har data for en målpassering på
formatet minutter, sekunder og hundredeler ([minutter, sekunder, hundredeler]).
"""
def all_lap_times(passing_times: list) -> list:
    """
    Tar en liste med tidspasseringer på formatet '[minutter, sekunder og hundredeler]'.
    Returnerer en liste med rundetider.
    """
    lap_times = []
    for i in range(0, len(passing_times)-1, 1):
        lap = lap_time(passing_times[i], passing_times[i+1])
        lap_times.append(lap)
    return lap_times

def main():

    print("\nTask 3a:")
    print(mshd2s(2, 10, 20))

    print("\nTask 3b:")
    lap = lap_time([0, 45, 20], [1, 14, 55])
    print(lap)

    print("\nTask 3c:")
    passings = [[0, 20, 0], [0, 50, 10], [1, 21, 21], [1, 53, 33]]
    times = all_lap_times(passings)
    print(times)

if __name__ == "__main__":
    main()
