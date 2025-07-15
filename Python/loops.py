board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for game in sport_games:
    print(game)

# Range
promise = "I will finish the python loops module!"

for x in range(5):
  print(promise)

# While
# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown=10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

# Iterate using while
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index=0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

# Breaks
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"


for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
      print("They have the dog I want!")
      break

# Conditionals on top of for
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age >= 21:
      print(age)

# Nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
  print(location)
  for sales in location:
    print(sales)
    scoops_sold += sales

print(scoops_sold)