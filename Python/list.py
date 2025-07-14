orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
print(orders)
orders.append("roses")
print(orders)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]


employee_four = employees[3]

print(employees[5])

# Your code below
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"

print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)


order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
new_store_order_list.remove("Mango")
print(new_store_order_list)

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]

incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken"

print(incoming_class) 


# Your code below:
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][-1] = False
customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim","X-Large",False]]
print(customer_data_final)


last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98,97,85,88]


gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])

print(gradebook)

gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[-1][-1] += 5
print(gradebook)

gradebook[2].remove(85)
print(gradebook)
gradebook[2].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)
print(list(range_five_three))
print(list(range_diff_five))


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)
big_range_length = len(list(big_range))
print(big_range_length)
long_list_len = len(long_list)
print(long_list_len)
# Your code below: 