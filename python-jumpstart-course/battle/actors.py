import random

class Creature:

    def __init__(self, the_name, the_level):
        self.name = the_name
        self.level = the_level

    def __repr__(self):
        return ("Creature {} of level {}".format(self.name, self.level))

    def get_defensive_roll(self):
        creature_roll = random.randint(1, 12) * self.level
        return creature_roll


class Wizard(Creature):

    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        heroWon = False
        print("The wizard {} attacks {}".format(self.name, creature.name))


        my_roll = random.randint(1, 12) * self.level
        creature_roll = self.get_defensive_roll()

        if my_roll >= creature_roll:
            print("The wizard defeated {}".format(creature.name))
            heroWon = True
            return heroWon
        else:
            print("The wizard has been DEFEATED")
            heroWon = False
            return heroWon



class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2

class Dragon(Creature):

    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name,level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = None

        if self.breaths_fire:
            fire_modifier = 5
        else:
            fire_modifier = 1

        scale_modifier = self.scaliness / 10

        return (base_roll * fire_modifier * scale_modifier)
