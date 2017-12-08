"""
Oppgave 4 – Mer programmering (40 %)
Vi har data fra en pulsklokke som er en vektor med hjertefrekvensen (antall pulsslag pr
sekund) for hver sekund av en treningstur. Data for en treningstur på 20 sekunder kan for
eksempel være:
[110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]
Det kan være hensiktsmessig å bruke funksjonene du lager utover i oppgaven. Du kan bruke
funksjoner fra andre deloppgaver selv om du ikke har klart å løse deloppgaven der du skal
lage funksjonen. Du kan forutsette at alle inndata er riktige.
"""

"""
Oppgave 4 a) (5 %)
Lag en funksjon pulsStatistikk(pulsData) som returnerer en liste med
gjennomsnittspuls, laveste puls og høyeste puls ut fra verdiene i innparameteren. Denne
deloppgaven skal løses uten bruk av innebygde funksjoner.
"""
def pulse_statistics(pulse_data: list) -> list:
    min_pulse = pulse_data[0]
    max_pulse = pulse_data[0]
    total_pulse = pulse_data[0]

    for i in range(1, len(pulse_data), 1):
        if pulse_data[i] < min_pulse:
            min_pulse = pulse_data[i]
        if pulse_data[i] > max_pulse:
            max_pulse = pulse_data[i]
        total_pulse += pulse_data[i]

    stats = [total_pulse / len(pulse_data), min_pulse, max_pulse]
    return stats

"""
Oppgave 4 b) (5 %)
Olympiatoppen definerer 5 treningssoner med utgangspunkt i en persons makspuls.
Treningssone 1 er belastning (hjertefrekvens) fra og med 60% til 72,5% av makspuls.
Treningssone 2 er puls fra og med 72,5% til 82,5%, treningssone 3 er puls fra og med 82,5%
til 87,5%, treningssone 4 er puls fra og med 87,5% til 92,5%, og treningssone 5 er puls fra og
med 92,5% av makspuls og høyere. Aktivitet med puls under 60% av makspuls regnes ikke
med i noen treningssone.
Lag funksjonen pulsSoneGrenser(maksPuls) som returnerer ei liste med
sonegrensene i pulsslag for en person med oppgitt makspuls
"""
def pulse_zone_limits(max_pulse: int) -> list:
    consts = [60.0, 72.5, 82.5, 87.5, 92.5]
    limits = []
    for const in consts:
        limit = (const / 100) * max_pulse
        limits.append(limit)
    return limits

"""
Oppgave 4 c) (15 %)
Lag en funksjon pulsSoner(maksPuls, pulsData). Funksjonen skal beregne hvor
stor andel i prosent av den totale treningstiden en person med oppgitt maksPuls og med
pulsdata som oppgitt i parameteren pulsData, har vært i hver av de fem treningssonene.
Prosenttall for de fem treningssonene skal returneres i ei liste med fem elementer.
"""
def pulse_zones(max_pulse: int, pulse_data: list) -> list:
    pulse_limits = pulse_zone_limits(max_pulse)
    pulse_limits.append(max_pulse)
    zone_counts = [0, 0, 0, 0, 0]
    for pulse in pulse_data:
        for i in range(1, len(pulse_limits), 1):
            if (pulse > pulse_limits[i-1]) and (pulse <= pulse_limits[i]):
                zone_counts[i-1] += 1
                break

    for i, zone_count in enumerate(zone_counts):
        zone_counts[i] = zone_counts[i] * (100 / len(pulse_data))

    return zone_counts

def main():
    pulse_data = [110, 118, 125, 127, 127, 130, 129, 131, 132, 134, 134, 135, 145, 157, 165, 172, 173, 178, 179, 178]

    print("\nTask 4a:")
    stats = pulse_statistics(pulse_data)
    print(stats)

    print("\nTask 4b: ")
    limits = pulse_zone_limits(188)
    print(limits)

    print("\nTask 4c:")
    zones = pulse_zones(188, pulse_data)
    print(zones)

if __name__ == "__main__":
    main()
