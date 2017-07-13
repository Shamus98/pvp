import random
 
class Character:
    def __init__(self, health, attack,armor):
        self.health = health
        self.attack = attack
        self.armor = armor
    def strike(self, target):
        damage = random.randint(0, self.attack - self.armor)
        target.health -= damage
 
 
class Window(Character):
 
    def die(self):
        print("nhtcr")
 
class Hero(Character):
    def __init__(self, health, attack, armor):
        super().__init__(health, attack, armor)
        self.count = 0
 
 
class Game:
    def start(self):
        hero = Hero(100, 50 , 10)
        window = Window(100, 20, 1)
        while True:
            k = random.randint(0,2)
            k1 = random.randint(0,2)
            k2 = random.randint(0,2)
            k3 = random.randint(0,2)
            hero.strike(window)
            window.strike(hero)
            if (k != 0): 
                hero.health += 10
            print()    
            if (k1 != 0):
                window.health -= 50
                print("Fireball")
            print()    
            if (k2 != 0):
                window.health -= 60
                print("Lighting punch")
            print()
            if (k3 != 0):
                hero.health -= 20
                print("Кара Билла Гейтса") 
            print()   
            print("Жизни игрока:", hero.health)
            print("Жизни окна:", window.health)
            input()
            if window.health <= 0:
                window.die()
                hero.count += 1
                window = Window(100, 20, 10)
            if hero.health <= 0:
                print("Ты сдох, но убил",hero.count, "окон")
                break
 
game = Game()
game.start()