# Printing to console
print("Hello, World!")

# Storing variables
my_String = "Hello, World!"
print(my_String)


# Changing the same variable
my_String = "Nicole"
print(my_String)
my_String = "Seongjun"
print(my_String)

# Integers
release_year = 2001
runtime = 3

# Float
rating_out_of_10 = 8.99

print(release_year)


# Math
print(25*68+13/28)

fence_width = 8
fence_length = 12

print(fence_width * fence_length)
print(fence_width ** 3)

#Modulo
first_order_remainder = 269%10
print(first_order_remainder)

# IF 
first_order_remainder = 269%10
second_order_remainder = 270%10
print(first_order_remainder)
print(second_order_remainder)

if first_order_remainder == 0:
  first_order_coupon = "yes"
else:
  first_order_coupon = "no"

if second_order_remainder == 0:
  second_order_coupon = "yes"
else:
  second_order_coupon = "no"

# string concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

#print(message)
print(message)

# Updating vars
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price = nice_sweater + fun_books + total_price
print("The total price is", total_price)

# super long string
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""


print(to_you)