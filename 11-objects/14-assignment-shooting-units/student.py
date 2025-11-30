# Write your code here
class Unit:
    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError()
        
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

    def get_health(self):
        return self.__health
    
    def get_firepower(self):
        return self.__firepower
    
    def get_armor(self):
        return self.__armor
    
    def shot_by(self, other):
        damage = other.get_firepower() - self.__armor
        
        if damage < 0:
            damage = 0
            
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0