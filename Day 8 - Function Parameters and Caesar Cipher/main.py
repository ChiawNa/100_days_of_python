# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

import math

number_of_cans = 0

def paint_calc(height, width, cover):
  number_of_cans = (test_h * test_w) / coverage
  number_of_cans_round = math.ceil(number_of_cans)
  print(f"You'll need {number_of_cans_round} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

