import random

avengers = 'Captain America Iron Man Thor Odinson Hulk Black Widow Hawkeye War Machine Vision Scarlet Witch Falcon Spider Man Ant Man Nebula Rocket'.split()
heroes = 'Animal Man Aqua Man Bat Woman Blue Devil Cain Cyclone Dawn Star Enchantress Green Lantern Heat Wave Katana Mr Freeze Nekron Poison Ivy'.split()

for i in avengers:
    print(random.choice(avengers), random.choice(heroes))
