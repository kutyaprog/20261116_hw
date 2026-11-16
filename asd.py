from random import randint
def fill():
    for i in range(10):
        scoreboard.append(round(randint(0,1000),-1))


def new_score():
    score = round(int(input("Mennyi lett az új highscore")))
    scoreboard.append(score)
    print(f"A(z) {score} pont bekerült a toplistára!")

def kiir():
    print(f"{scoreboard} {len(scoreboard)}", sep=", ")
    
def kereses():
    kerse = input("Mit keres? ")
    if kerse in scoreboard:
        print(f"Benne van a scoreboardban a(z) {kerse}")
    else:
        print("Nincs ilye score")

def sorting():
    scoreboard.sort(reverse=True)
    print(scoreboard)

def remo():
    kerse = input("Mit akar kidobni? ")
    if kerse in scoreboard:
        scoreboard.remove(kerse)
    else:
        print("Ezt elhagytad...")

def db_reset():
    scoreboard.clear

def main():
    fill()
    new_score()
    sorting()
    kiir()
    kereses()
    remo()
    db_reset()
    


scoreboard = []


main()
