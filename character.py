import random


class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.initial_power = attack_power  # remember the starting power

    def attack(self, other):
        # damage is a random 30%-90% of the initial power
        self.attack_power = round(random.uniform(0.3, 0.9) * self.initial_power, 1)
        other.hp -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {round(self.hp, 1)} HP"