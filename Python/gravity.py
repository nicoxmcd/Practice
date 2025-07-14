print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = int(input("Which planet do you want to know about?"))

# Write an if statement below:
if planet == 1:
  print("Venus' relative gravity: 0.91")
elif planet == 2:
  print("Mars' relative gravity: 0.38")
elif planet == 3:
  print("Jupiter's relative gravity: 2.34")
elif planet == 4:
  print("Saturn's relative gravity: 1.06")
elif planet == 5:
  print("Uranus' relative gravity: 0.92")
elif planet == 6:
  print("Neptune's relative gravity: 1.19")
else:
  print("Invalid.")