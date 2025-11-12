def ekafunktio():
    print("Tämä on ensimmäinen funktio.")

def tokafunktio(sana):
    sana = "lisätään" + sana
    print(sana)

def kolmasfunktio(sana):
    return "lisätään" + sana

def neljasfunktio():
    return "Tämä on neljäs funktio."

def main():
    print("Tervetuloa syksyn 2025 ohjelmaan!")
    ekafunktio()
    tokafunktio("Toka funktio tulostaa tämän")
    kolmannenpalautus = kolmasfunktio("Kolmas funktio palauttaa tämän")
    print(kolmannenpalautus)
    print(neljasfunktio())

if __name__ == "__main__":
     main()