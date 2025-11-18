from datetime import datetime

def hae_varausnumero(varaus):
    varausnumero = int(varaus[0])
    print(f"Varausnumero: {varausnumero}")
    
def hae_varaaja(varaus):
    nimi = str(varaus[1])
    print(f"Varaaja: {nimi}")

def hae_paiva(varaus):
    paivamaara = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    suomalainenpvm = paivamaara.strftime("%d.%m.%Y")
    print(f"Päivämäärä: {suomalainenpvm}")
    
def hae_aloitusaika(varaus):
    aloitusaika = datetime.strptime(varaus[3], "%H:%M").time()
    suomalainenaika = aloitusaika.strftime("%H.%M")
    print(f"Aloitusaika: {suomalainenaika}")
       
def hae_tuntimaara(varaus):
    tuntimaara = int(varaus[4])
    print(f"Tuntimäärä: {tuntimaara}")
    
def hae_tuntihinta(varaus):
    tuntihinta = float(varaus[5])
    print(f"Tuntihinta: {tuntihinta:.2f}".replace('.',',') + " €")
  
def laske_kokonaishinta(varaus):
    kokonaishinta = int(varaus[4]) * float(varaus[5])
    print(f"Kokonaishinta: {kokonaishinta:.2f}".replace('.',',') + " €")
    
def hae_maksettu(varaus):
    maksettu = varaus[6]
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")

def hae_kohde(varaus):
    kohde = str(varaus[7])
    print(f"Kohde: {kohde}")
    
def hae_puhelin(varaus):
    puhelin = str(varaus[8])
    print(f"Puhelin: {puhelin}")
    
def hae_sahkoposti(varaus):
    sahkoposti = str(varaus[9])
    print(f"Sähköposti: {sahkoposti}")
    
def main():
    varaukset = "varaukset.txt"

    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
    
if __name__ == "__main__":
    main()