"""
Oppgave 4: Mer programmering (40%)
UKA trenger et system for å styre billettsalget. Du har meldt deg frivillig til å hjelpe til.
(Hvis du ikke klarer å løse en deloppgave kan du likevel bruke funksjoner fra tidligere
deloppgaver som om de er riktig implementert.) Det kan være lurt å kommentere koden.
"""

"""
Oppgave 4a (5%)
Lag en funksjon, payment, som tar inn billettpris og antall billetter og returnerer hvor mye kunden
skal betale. Hvis man har kjøpt mer enn 3 billetter skal man få 10% rabatt på alle billettene.
"""
def payment(ticket_price: int, tickets: int) -> float:
    rebate = 0.0
    if tickets >= 3:
        rebate = 0.10
    total_price = (ticket_price * tickets * (1.0 - rebate))
    return total_price

"""
Oppgave 4b (5%)
Anta at det finnes en tekstfil, prices.txt, som inneholder konsertnavn og billettpris for
konserten. Hver konsertoppføring er lagret på en linje i filen, der konsertnavn står først og pris
kommer etter konsertnavnet separert med et semikolon (;).
Skriv en funksjon, get_price, som tar inn et konsertnavn og returnerer prisen for denne
konserten. (Du må ta hensyn til tilfellet der konsernavnet ikke finnes!). Hvis konserten ikke finnes
returnerer funksjonen prisen -1. 
"""
def get_price(concert_name: str) -> int:
    concerts_file = open("prices.txt")
    concert_list = concerts_file.read().split("\n")
    concerts_file.close()

    concerts = {}
    for concert in concert_list:
        concert = concert.split(";")
        concerts[concert[0]] = concert[1]

    if concert_name in concerts:
        return int(concerts[concert_name])
    else:
        return -1

"""
Oppgave 4c (5%)
Lag en funksjon, ticket, som tar inn kjøpers navn, konsertnavn og antall billetter som
argumenter. Bruk funksjonen i 4a til å generere pris som skal brukes i billett-teksten denne
funksjonen skal generere. Billetten skal inneholde kjøpers navn, hvilken konsert, antall og totalpris.
Billettprisen for konserten skal hentes fra filen prices.txt som ble brukt i oppgave 4b. Bruk
funksjonene du skrev i 4a og 4b i denne oppgaven! (Hvis du ikke har løst 4a og 4b, kan du
forutsette at de funksjonene finnes).
"""
def ticket(buyer_name: str, concert_name: str, ticket_count: int):
    concert_price = get_price(concert_name)
    total_price = payment(concert_price, ticket_count)

    width = 41
    w_d = width + "d"
    name = "Navn:\t\t{}".format(buyer_name)
    concert = "Konsert:\t\t{}".format(concert_name)
    count = "Antall:\t\t{}".format(ticket_count)
    total = "Total:\t\t{}".format(total_price)
    print("*"*width)
    print(format("Uka 2015"), w_d)
    print("*"*width)
    print(format(name, w_d))
    print(format(concert, w_d))
    print(format(count, w_d))
    print(format(total, w_d))

"""
Oppgave 4d (10%)
Lag en funksjon, write_to_file, som får billettinformasjon fra funksjonen i oppgave 4b:
(navn, konsertnavn og antall billetter) og lagrer denne til en fil (concerts.txt). Filen skal
inneholde 1 linje for hver billettransaksjon. Linjene skal bestå av konsertnavn, antall billetter,
totalpris og kundenavn. Hvert element på linjen skal være skilt med et semikolon ( ;). Filnavnet skal
være med som innparameter til funksjonen. Filen skal oppdateres underveis og skal ikke slettes hver
gang den åpnes.
"""
def write_to_file(name: str, concert_name: str, ticket_count: int, file_name: str):
    concert_price = get_price(concert_name)
    total_price = payment(concert_price, ticket_count)
    transaction = "{};{};{};{}".format(concert_name, ticket_count, total_price, name)

    transactions_file = open(file_name, "w")
    transactions_file.write(transaction)
    transactions_file.close()

"""
Oppgave 4e (15%)
Lag et menystyrt program som lar deg hente fra filen concerts.txt hvor mange billetter som er
solgt til en gitt konsert, hvor stort beløp en gitt konsert har innbrakt, og totalinntekt for hele
arrangementet. 
"""
def get_transactions(file_name: str):
    transactions_file = open(file_name)
    transactions = transactions_file.read().split("\n")
    transactions_file.close()

    return list(map(lambda transaction: transaction.split(";"), transactions))

def concert_earnings(transactions: list):
    concert_name = input("Name of the concert you want to find earnings for: ")
    filtered = filter(lambda transaction: transaction[0] == concert_name, transactions)
    earnings = sum(map(lambda transaction: float(transaction[2]), filtered))
    print("Total earnings: {}".format(earnings))

def total_earnings(transactions: list):
    earnings = sum(map(lambda transaction: float(transaction[2]), transactions))
    print("Total earnings: {}".format(earnings))

def tickets_for_concerts(transactions: list):
    tickets = sum(map(lambda transaction: float(transaction[1]), transactions))
    print("Total tickets: {}".format(tickets))


def main():
    print("Velkommen til konsertapplikasjonen!")
    states = [
        "0. Gå ut av applikasjonen.",
        "1: Antall biletter for konsert.",
        "2. Totalt beløp for konsert.",
        "3. Total inntekt for hele arrangementet."
    ]
    functions = {
        0: exit,
        1: tickets_for_concerts,
        2: concert_earnings,
        3: total_earnings
    }
    transactions = get_transactions("concerts.txt")
    print("\n".join(states))
    state = int(input("Hvilken funksjon vil du bruke?\t"))
    while state != 0:
        functions[state](transactions)
        state = int(input("Hvilken funksjon vil du bruke?\t"))

if __name__ == "__main__":
    main()
