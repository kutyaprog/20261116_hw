from random import uniform

metarologia = []
def fill():
    for i in range(10):
        metarologia.append(round(uniform(0,1000),-1))


def uj_homerseklet_rogzitese():
    meres = float(input("Mérés edremény? "))
    metarologia.append(meres)
    print(f"A(z) {meres} Rögzült!")

def kiir():
    print(*metarologia, len(metarologia), sep=", ")
    osszeg = 0
    for i in range(len(metarologia)):
        osszeg += metarologia[i]
    print(osszeg / len(metarologia))
        
    
def kereses():
    kerse = input("Mit keres? ")
    if kerse in metarologia:
        print(f"Benne van a metarologiaban a(z) {kerse}")
    else:
        print("Nincs ilye meres")

def sorting():
    metarologia.sort(reverse=False)
    print(metarologia)

def remo():
    kerse = input("Mit akar kidobni? ")
    if kerse in metarologia:
        metarologia.remove(kerse)
    else:
        print("lyen mérési adat nem is szerepelt a rendszerben!")

def db_reset():
    metarologia.clear

def main():
    fill()
    uj_homerseklet_rogzitese()
    sorting()
    kiir()
    kereses()
    remo()
    db_reset()
    





main()
