#import pandas as pd
#import numpy as np
#from numpy.random import seed
#from numpy.random import randint
from numpy.random import choice

class Quina():

  def __init__(self):
    self.bets = []
    self.prize_value = 10000
    self.base_price = 2.50
    self.bet_min = 5
    self.bet_max = 15
    self.bet_range_start = 1
    self.bet_range_end = 80
    #TODO porcentagens de vitória

  def read_bets(self, bets):
    err = []
    try:
      for i in bets:
        if len(i) > self.bet_max or len(i) < self.bet_min:
          err.append(i)
          continue
        if min(i) < self.bet_range_start or max(i) > self.bet_range_end:
          err.append(i)
          continue
        if len(dict.fromkeys(i).keys()) != len(i): #this is to check if are there any equal values in the bet
          err.append(i)
          continue

        bet_price = self.calculate_price(len(i))
        self.prize_value += bet_price
        self.bets += [i]

        #self.prize_value = self.prize_value + round(self.prize_value * 0.4335, 2) this is wrong

      return {"bets": self.bets, "current_total_prize": self.prize_value, "err": err}

    except Exception as e:
      return f"An error ocurred at function read_bets: {e}"

  def factorial(self, num):
    if num > 1:
      return num*(self.factorial(num-1))
    else:
      return 1

  def calculate_price(self, num_of_numbers):
    com = (self.factorial(num_of_numbers)) / (self.factorial(self.bet_min) * self.factorial(num_of_numbers - self.bet_min))
    return self.base_price * com

  def calculate_probability(self):
    try:
      total_poss_max_win = (self.factorial(self.bet_range_end)) / (self.factorial(self.bet_min) * self.factorial(self.bet_range_end - self.bet_min))
      total_poss_1 = (self.factorial(self.bet_range_end)) / (self.factorial(self.bet_min - 1) * self.factorial(self.bet_range_end - (self.bet_min - 1)))
      total_poss_2 = (self.factorial(self.bet_range_end)) / (self.factorial(self.bet_min - 2) * self.factorial(self.bet_range_end - (self.bet_min - 2)))
      total_poss_3 = (self.factorial(self.bet_range_end)) / (self.factorial(self.bet_min - 3) * self.factorial(self.bet_range_end - (self.bet_min - 3)))
      total_poss_4 = (self.factorial(self.bet_range_end)) / (self.factorial(self.bet_min - 4) * self.factorial(self.bet_range_end - (self.bet_min - 4)))

      probability = {f"{self.bet_min}_chance": (1 / total_poss_max_win),
                     f"{self.bet_min - 1}_chance": (1 / total_poss_1),
                     f"{self.bet_min - 2}_chance": (1 / total_poss_2),
                     f"{self.bet_min - 3}_chance": (1 / total_poss_3),
                     f"{self.bet_min - 4}_chance": (1 / total_poss_4)}

      return probability

    except Exception as e:
      return f"An error ocurred at function calculate_probability: {e}"

  def execute_drawn(self):
    try:
      drawn_values = list((choice(range(self.bet_range_start, self.bet_range_end + 1), self.bet_min, replace=False)))
      drawn_values = [int(k) for k in drawn_values]
      results = {"drawn_values": drawn_values, f"{self.bet_min}_winner": [], f"{self.bet_min-1}_winner": [], f"{self.bet_min-2}_winner": [], f"{self.bet_min-3}_winner": [], f"{self.bet_min-4}_winner": [], "non_winners": []}

      for i in self.bets:
        count = 0
        for ii in i:
          if ii in drawn_values:
            count += 1
        try:
          if count > 5:
            count = 5
          results[f"{count}_winner"] += [i]
        except:
          results["non_winners"] += [i]

      self.bets = []
      return results

    except Exception as e:
      return f"An error ocurred at function execute_drawn: {e}"
