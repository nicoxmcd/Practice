my_name = "Nicole"
first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]


first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]
new_account = account_generator(first_name, last_name)


first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]
temp_password = password_generator(first_name, last_name)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]


first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

password = "theycallme\"crazy\"91"


def get_length(word):
  length =0
  for letter in word:
    length += 1
  return length
  
final_length = get_length("onomopeoai")

print(final_length)

def letter_check(word, letter):
  for x in word:
    if x == letter:
      return True
    else:
      continue
  return False


def contains(big_string, little_string):
  return little_string in big_string
contains("watermelon", "melon")


def common_letters(string_one, string_two):
  letters = []
  for letter_one in string_one:
    if (letter_one in string_two) and not (letter_one in letters):
      letters.append(letter_one)
  return letters

def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = ""
  for letter in range(0,len(user_name)):
    password += user_name[letter - 1]
  return password

poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

line_one = "The sky has given over"
line_one_words = line_one.split()