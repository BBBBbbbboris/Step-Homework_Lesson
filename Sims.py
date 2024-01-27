import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def day_indexes(self):
        pass
    def is_alive(self):
        pass
    def lives(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return  True
        else:
            print("The car cannot move!")
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.water = 0



brands_of_car = {"BMW" :{"fuel": 100, "strenght": 120, "consumption": 14},
                 "Lada" :{"fuel": 80, "strenght": 40, "consumption": 12},
                 "Ford" :{"fuel": 60, "strenght": 80, "consumption": 8},
                 "Ferrari" :{"fuel": 50, "strenght": 90, "consumption": 16}}
