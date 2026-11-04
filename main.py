from character import Character


def main():
    hero = Character("Knight", 60, 8)
    enemies = [
        Character("Goblin", 20, 3),
        Character("Orc", 25, 4),
    ]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(e.is_alive() for e in enemies):
        # hero attacks the first enemy that is still alive
        target = next(e for e in enemies if e.is_alive())
        hero.attack(target)

        # every surviving enemy attacks the hero
        for enemy in enemies:
            if enemy.is_alive() and hero.is_alive():
                enemy.attack(hero)

        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("The enemies win!")


if __name__ == "__main__":
    main()