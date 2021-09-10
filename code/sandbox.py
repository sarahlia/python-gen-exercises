# Section 1: Hello World
my_name = "Sarah"
print("Hello and welcome " + my_name + "!")

# This variable is used to count the number of times anyone tweets the word persnickety
persnickety_count = 0

def old_sloppy_code():
  return "old code. needs refactoring"

def new_clean_code():
  return "new code, much better."

# useful_value = old_sloppy_code()
useful_value = new_clean_code()
print(useful_value)

# from Mary Shelley's Frankenstein
print("There is something at work in my soul, which I do not understand.")

print("Hello world!")

# Section 2: Control Flow
example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"

# relational operators
statement_one = True

statement_two = False

statement_three = True

# Section 3: Lists
heights = [61, 70, 67, 64]
heights.append(65)

print(heights)

broken_heights = [65, 71, 59, 62]

ints_and_strings = [1, 2, 3, "four", "five", "Luke", "Skywalker"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

my_empty_list = []

# Section 4: Loops
# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)

# Section 5: Functions
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  
directions_to_timesSq()