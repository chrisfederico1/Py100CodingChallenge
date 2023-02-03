################### Scope ####################

# enemies = 1
# 
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# 
# 
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global scope
player_health = 10


def drink_potion():
    """ This print postion_strenght  """
    potion_strenght = 2
    print(potion_strenght)


drink_potion()
