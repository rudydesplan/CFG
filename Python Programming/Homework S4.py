# Question 1
# I have a list of things I need to buy from my supermarket of choice.
# I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer to what I was expecting?
# What is the mistake? How do I fix it?
# Answer : A List always start from the index = 0 and not index = 1

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]
print(shopping_list[0])

# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell.
# Finish the program by asking the user to input an item and then output its price.

chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}
type = input("What type of chocolate do you want ?")
price = chocolates[type]
print(f"The price of is {type} chocolate is : {price}")

# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket. It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random
from random import randint

my_lottery_ticket = []
for number in range(0,7):
    x = input("Please Enter your lottery number")
    my_lottery_ticket += [x]
print(my_lottery_ticket)

winning_ticket = []
for number in range(0,7):
    y = randint(0, 100)
    winning_ticket += [y]
print(winning_ticket)

matching_numbers = []
for number in my_lottery_ticket:
    if number in my_lottery_ticket:
        matching_numbers += [number]
print(matching_numbers)

matching_numbers_count = len(matching_numbers)

Prize = {
    0 : "Sorry, no matching numbers.",
    1 : "1 matching number. No win.",
    2 : "2 matching numbers. No win.",
    3 : "3 matching numbers. You won £20.",
    4 : "4 matching numbers. You won £40.",
    5 : "5 matching numbers. You won £100.",
    6 : "6 matching numbers. You won £10'000!",
    7 : "7 matching numbers. You won £1'000'000!!!"
}

print(Prize[matching_number_count])