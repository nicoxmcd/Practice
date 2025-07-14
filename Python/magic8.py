from random import randint

name = input("What is your name?")
question = input("What is your question?")
magic_8_string = "Magic 8-Ball's answer: "

if question == "":
  print("You must ask a question.")
  exit()

if name == "":
  ask_string = "Question: " + question
else:
  ask_string = name + " asks: " + question

answer_val = randint(1,10)

match answer_val:
  case 1:
    answer = "Yes - definitely"
  case 2:
    answer = "It is decidedly so"
  case 3:
    answer = "Without a doubt"
  case 4:
    answer = "Reply hazy, try again"
  case 5:
    answer = "Better not tell you now"
  case 6:
    answer = "My sources say no"
  case 7:
    answer = "Outlook not so good"
  case 8: 
    answer = "Very doubtful"
  case 9:
    answer = "Ask again later"
  case 10:
    answer = "Ask God"

print(ask_string)
print(magic_8_string + answer)