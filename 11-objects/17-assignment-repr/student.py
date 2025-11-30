# Write your code here
class Pokemon:
    def __init__(self, number, name, type):
        self.number = number
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Pokemon({self.number}, \"{self.name}\", \"{self.type}\")"


bulbasaur = Pokemon(1, "Bulbasaur", "Grass-Poison")
print(bulbasaur.name)

charmander = Pokemon(4, "Charmander", "Fire")
print(charmander.type)

squirtle = Pokemon(7, "Squirtle", "Water")
print(squirtle.number)