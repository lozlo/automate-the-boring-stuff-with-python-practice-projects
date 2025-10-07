# fantasy_game_inventory.py
# A simple inventory management system for a fantasy game.


# def display_inventory(inventory):
#     print("Inventory:")

#     item_total = 0
#     for k, v in inventory.items():
#         item_total += v
#         print(str(v) + ' ' + k)

#     print("Total number of items: " + str(item_total))


# def add_to_inventory(inventory, added_items):
#     for i in added_items:
#         inventory.setdefault(i, 0)
#         inventory[i] += 1
#     return inventory


# def main():
#     stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#     dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#     inv = add_to_inventory(stuff, dragon_loot)
#     display_inventory(inv)


# if __name__ == "__main__":
#     main()

# Refactored to improve readability and maintainability


from collections import Counter


def display_inventory(inventory):
    print("Inventory:")
    item_total = sum(inventory.values())
    
    for item, count in inventory.items():
        print(f"{count} {item}")
    
    print(f"Total number of items: {item_total}")


def add_to_inventory(inventory, added_items):
    inventory_counter = Counter(inventory)
    loot_counter = Counter(added_items)
    inventory_counter.update(loot_counter)
    return dict(inventory_counter)


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    inv = add_to_inventory(stuff, dragon_loot)
    display_inventory(inv)


if __name__ == "__main__":
    main()
