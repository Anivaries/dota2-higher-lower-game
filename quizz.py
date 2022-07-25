from data import hero_dict, bracket_list
from random import *


class QuizBrain():

    
    def __init__(self) -> None:
        pass
        
#------------------RANDOMIZING HEROES AND BRACKET------------------#
    def random_picks(self):
        self.bracket_pick = choice(bracket_list)
        self.hero_name_one = choice(list(hero_dict))
        self.hero_name_two = choice(list(hero_dict))
        self.winrate_hero_one = float(hero_dict[self.hero_name_one][bracket_list.index(self.bracket_pick)])
        self.winrate_hero_two = float(hero_dict[self.hero_name_two][bracket_list.index(self.bracket_pick)])
        self.hero_one_img = hero_dict[self.hero_name_one][5]
        self.hero_two_img = hero_dict[self.hero_name_two][5]

        if self.winrate_hero_one > self.winrate_hero_two:
            self.winner = self.hero_name_one
        else: 
            self.winner = self.hero_name_two
        if self.hero_name_two == self.hero_name_one:
            self.random_picks()
        return (f"Which hero has higher winrate in {self.bracket_pick} bracket:\n {self.hero_name_one} or {self.hero_name_two}? ")
#------------------RANDOMIZING HEROES AND BRACKET------------------#

        