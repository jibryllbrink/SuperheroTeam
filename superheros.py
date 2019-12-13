import random

class Ability:
    def __init__(self, name, max_damage):

        self.name = name
        self.max_damage = max_damage

    def attack(self):

        random_value = random.randint(0,self.max_damage)
        return random_value

class Armor:
     def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

     def block(self):

        return random.randint(0, self.max_block)

class Hero:

    def __init__(self, name, starting_health=100):
   
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)
    def add_deaths(self, num_deaths):
        self.deaths = num_deaths
    def defend(self, damage_amt):
        total_block = 0
        for total_block in self.armors:
            total_block += damage_amt.block()
        return total_block
    def take_damage(self, damage):
        defense = self.defend(damage)    
        self.current_health -= damage - defense
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    def is_dead(self):
        if self.current_health <= 0:
            return True
        else:
            return False
    def add_kill(self, num_kills):
        self.kills += num_kills
        return self.kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        return self.deaths
    
    def fight(self, enemy):
 
        while self.is_alive() and enemy.is_alive():
            self.take_damage(enemy.attack())
            enemy.take_damage(self.attack())
            
        if self.is_alive() is False:
            self.add_deaths(1)
            enemy.add_kill(1)
            return print(f"{enemy.name} wins")
        elif enemy.is_alive() is False:
            self.add_kill(1)
            enemy.add_deaths(1)
            return print(f"{self.name} wins")
        









if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Wonder Woman")
    enemy = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero.add_ability(ability1)
    hero.add_ability(ability2)
    enemy.add_ability(ability3)
    enemy.add_ability(ability4)
    hero.fight(enemy)