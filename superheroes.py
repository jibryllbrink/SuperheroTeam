import random

class Arena:
    def __init__(self):
        '''Instantiate properties'''
        self.team_one = Team("team one")
        self.team_two = Team("team two")
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    def create_weapon(self):
        create_weapon = input("Name a weapon:"  )
        weapon_dmg = int(input("Weapon damage (integer): "))
        return Weapon(create_weapon, weapon_dmg)
    def create_armor(self):
        create_armor = input("Name a armor:"  )
        armor_dmg = int(input("Armor damage (integer): "))
        return Armor(create_armor, armor_dmg)
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero
    def build_team_one(self):
            self.team_one_name = input(f"Enter Team One's name: ")
            self.team_o = Team(self.team_one_name)
            team_one_superheros = int(input(f"Amount of superheros on {self.team_one_name}: "))
            for i in range(team_one_superheros):
                hero = self.create_hero()
                self.team_o.add_hero(hero)
    def build_team_two(self):
        self.team_two_name = input("Enter Team Two's name: ")
        self.team_t = Team(self.team_two_name)
        team_two_superheros = int(input(f"Amount of superheros on {self.team_t}: "))
        for i in range(team_two_superheros):
            hero = self.create_hero()
            self.team_t.add_hero(hero)
    def team_battle(self):
        self.team_one.attack(self.team_two)
    def show_stats(self):
        #Prints team statistics to the terminal
        print("\nStats: ")
        self.team_one.stats()
        self.team_two.stats()
        if len(self.team_one.heroes) > 0:
            print(self.team_one.name + "wins")
        else:
            print(self.team_two.name + "wins")


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

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

class Hero:
    def __init__(self, name, starting_health=100):  
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    def add_armor(self, armor):
        self.armors.append(armor)
    def add_deaths(self, num_deaths):
        self.deaths = num_deaths
    def defend(self, damage_total=0):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    def take_damage(self, damage):
        defense = self.defend(damage)    
        self.current_health -= damage - defense
        return self.current_health
    def is_alive(self): 
        if self.current_health > 0:
            return True
        else:
            return False
    def is_not_alive(self):
        if self.current_health <= 0:
            return True
        else:
            return False
    def add_kill(self, num_kills):
        self.kills += num_kills
        #return self.kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        #return self.deaths
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


class Team:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.heroes = list()
    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
            if not foundHero:
                return False
    def view_all_heroes(self):
        for superheros in self.heroes:
            print(superheros.name)
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    def revive_superheros(self):
        #Resets all superheros health to starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()
        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)
        while len(living_heroes) > 0 and len(living_opponents)> 0:

            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the superheroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight

            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            random_hero.fight(random_opponent)
            if random_hero.is_alive():
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)
    def is_alive(self):
        #Checks if they are alive
        is_alive = []
        for hero in self.heroes:
            if hero.is_alive == True:
                is_alive.append(hero)
            return is_alive


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

if __name__ == "__main__":
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

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        
        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()