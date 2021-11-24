# Homework: Session 3

# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

Rain = input(" Is it raining ? \n Anser with y for Yes or n for No ." )
if Rain == 'y' :
    print("Take an umbrella \.")
else :
    print('You don\'t need an umbrella.')

# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
# written a program to check that I can afford the cost, but something doesn't seem right.

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money < boat_cost:
    print('You can afford the boat hire')
else :
    print('You cannot afford the board hire')

# Question 3
# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth Century, Seventies")

Year = int(input("What is the book year ?"))
Century = Year // 100
if Century == 18 :
        c = "Eighteenth"
elif Century == 19 :
        c = "Nineteenth"        
else:
        c = " "
Decade = ( Year - Century * 100 ) // 10
if Decade == 1 :
        d = "Tens"
elif Decade == 2 :
        d = "Twenties"     
elif Decade == 3 :
        d = "Thirties"          
elif Decade == 4 :
        d = "Forties"          
elif Decade == 5 :
        d = "Fifties"          
elif Decade == 6 :
        d = "Sixties"          
elif Decade == 7 :
        d = "Seventies"  
elif Decade == 8 :
        d = "Eighties"     
elif Decade == 9 :
        d = "Nineties"
else:
        d = " "
print(f"{c} Century,{d}")