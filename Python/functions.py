def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:
directions_to_timesSq()

print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()


#  Using parameters
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate,trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = hotel_total + car_rental_total + plane_ticket_price
  
  print(trip_total)
  return trip_total

# Step 5: call your function
calculate_expenses(200,100,100,5)

# Positional argument and keyword arguments
# Write your code below:
def trip_planner(first_destination="Iceland", second_destination="India", final_destination="Germany"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("Brooklyn", "Queens")

# Mulitple functions

current_budget = 3500.75
shirt_expense = 9

def deduct_expense(budget, expense):
  return budget - expense

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)
# Write your code below: 


# Multiple returns
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)

# trip planner
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  time = str(estimated_time)
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + time + " hours")

trip_planner_welcome("nicole")
estimate = estimated_time_rounded(2.2)
destination_setup("Bergen County", "Ocean County", estimate)