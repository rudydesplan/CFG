# Question 1   : Explain what this program does
#   for number in range(100):
#       output = 'o' * number
#   print(output)
# This program will print in 99 rows the letter 'o' , each time increasing by 1 the number of 'o' letter . The Last row has 99 'o' .

#  Question 2
#  Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written
#  this code to calculate VAT and need your help to fix it.

def calculate_vat (amount):
    vat = amount * 1.2
    return vat

total = calculate_vat(100)
print(total)

#   Question 3
#   Using the turtle module, write a program to draw a house. The house should at least have a roof, a
#   door and some windows. Feel free to play around with the design of your house.

import turtle
  
  
t = turtle.Turtle()
  
# for background
screen = turtle.Screen()
screen.bgcolor("yellow")
  
#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(1)
  
# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()
  
# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()
  
# for door and
# windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
turtle.done()