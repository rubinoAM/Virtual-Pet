from Pet import Pet, personalities
from random import *

name = input("Enter a name for your pet > ")
pers_sel = randrange(0,5)
personality = personalities[pers_sel]
weight = randrange(3,10)

a_pet = Pet(name,personality,weight)

print ("Your pet's name is %s. They are of the %s personality type, and they weighed %s pounds at birth." % (a_pet.name,a_pet.personality,a_pet.weight))