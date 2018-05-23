import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()

def print_header():
    print("-------------------------")
    print("     WIZARD GAME APP     ")
    print("-------------------------")

def game_loop():

    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 30, True),
        Wizard("Evil Wizard", 1000),

        ]

    hero = Wizard("Gandols", 75)

    print (creatures)

    while True:
        active_creature = random.choice(creatures)
        print("{} of level {} has appeared from the forrest\n" .format(active_creature.name, active_creature.level))

        userInput = input ("Do you [A]ttack, [R]un away or [L]ook around: ")
        userInput = userInput.upper()

        if userInput == "A":
            heroWon = hero.attack(active_creature)
            if heroWon:
                creatures.remove(active_creature)
            else:
                print("{} is knocked down and needs time to recover".format(hero.name))
                time.sleep(5)
                print("The {} returns..".format(hero.name))

        elif userInput == "R":
            print("Print the wizard has become unsure of him and flees....")
        elif userInput == "L":
            print("The wizard {} looks around and sees: " .format(hero.name))
            for c in creatures:
                print("*** A {} of level {} ***" .format(c.name,c.level))

        else:
            print("Exiting game....")
            break

        if not creatures:
            print(" You defeated all the creatures.")
            break

if __name__ == "__main__":
    main()