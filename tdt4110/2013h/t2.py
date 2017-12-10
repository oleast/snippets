"""
Oppgave 2: Grunnleggende programmering (20%)
I et parti sjakk belønnes vinneren med 1 poeng, taperen får 0 poeng, og ved remis (uavgjort) får
begge ½ poeng hver. En sjakk-kamp spilles i et på forhånd bestemt antall partier, n. Trondheim
sjakkforening (TSF) skal arrangere en kamp mellom de to stormestrene Carl Magnøssen (spiller nr.
1) og Sjakkma Ghandi (spiller nr. 2). TSF trenger din hjelp til å lage et program for å administrere
kampen. I stedet for navnene til spillerne brukes kun numrene (1 og 2).
"""

"""
procedure chess_match()
    Sett total_score1 ⟵ 0 # Totalpoeng til spiller 1
    Sett total_score2 ⟵ 0 # Totalpoeng til spiller 2

    Spør brukeren om hvor mange partier som skal spilles i kampen
    Sett num_games ⟵ antall partier

    Hvis brukeren gir et tall<1, skriv ut "Så kjedelig, da blir det ingen kamp!"
    Ellers, så lenge det er partier igjen å spille:
        Skriv ut "Parti" og nummeret på partiet

        Spør brukeren om antall poeng til spiller 1 i partiet
        Sett score1 ⟵ antall poeng til spiller 1 i partiet

        Spør brukeren om antall poeng til spiller 2 i partiet
        Sett score2 ⟵ antall poeng til spiller 2 i partiet

        Sett total_score1 ⟵ total_score1 + score1
        Sett total_score2 ⟵ total_score2 + score2

    Skriv ut "Kampen er slutt!"
    Skriv ut "Spiller 1 fikk " fulgt av totalpoengene til spiller 1 og "poeng."
    Skriv ut "Spiller 2 fikk " fulgt av totalpoengene til spiller 2 og "poeng."
"""
def chess_match():
    total_score1 = 0
    total_score2 = 0

    num_games = int(input("Hvor mange partier som skal spilles i kampen: "))
    parties = num_games

    if num_games < 1:
        print("Så kjedelig, da blir det ingen kamp!")
    else:
        while parties > 0:
            print("Parti {}".format(num_games))

            score1 = int(input("Antall poeng til spiller 1 i partiet: "))
            score2 = int(input("Antall poeng til spiller 2 i partiet: "))

            total_score1 += score1
            total_score2 += score2

            parties -= 1

        print("Kampen er slutt!")
        print("Spiller 1 fikk {} poeng.".format(total_score1))
        print("Spiller 2 fikk {} poeng.".format(total_score2))

"""
Oppgave 2b (3%)
Den spilleren som oppnår mer enn halvparten av de mulige poengene (dvs har n/2+0.5 eller fler
poeng hvis kampen er inntil n partier) vinner kampen - da trenger ikke de gjenstående partiene å
spilles. Hvis alle n partier er blitt spilt og de to spillerne har like mange poeng, slutter kampen
uavgjort og man må spille ekstrapartier for å kåre en vinner. Hvis kampen er inntil 12 partier, kan
den ende 6-6 med ekstraparti, eller ved at en av spillerne oppnår 6.5 eller 7 poeng (etter 7-12
partier).
Lag funksjonen
    end_of_match(num_games, game, total_score1, total_score2)
som sjekker om kampen er slutt og som rapporterer om hvem som i så fall vant den. Funksjonen må
altså sjekke om totalpoengene for en spiller er så høye at spilleren har vunnet kampen. Funksjonen
tar 4 argumenter, to heltall (num_games og games) og to flyttall (total_Score1 og
total_score2), og returnerer enten 0 hvis kampen fortsatt pågår, nummeret til den spilleren
som har vunnet kampen (1 eller 2) hvis kampen er avgjort, og 3 hvis kampen sluttet uavgjort. 
"""
def end_of_match(num_games: int, game: int, total_score1: float, total_score2: float) -> int:
    pass
