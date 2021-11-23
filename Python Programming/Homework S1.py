# Question 1

chairs = 15      #previously : chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# Question 2

my_name = "Penelope"    #previously : my_name = Penelope
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# Question 3

box_of_eggs = int(input("How many box of eggs do you have ?"))
eggs_needed = int(input("How many eggs do you need for each omelette ?"))
total_eggs = 6* box_of_eggs
omelette = total_eggs // eggs_needed
eggs_left = total_eggs % eggs_needed
print(f"You can make {omelette} omelettes with {box_of_eggs} box_of_eggs , there will be {eggs_left} eggs left ")