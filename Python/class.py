class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
      

class Grade:
  minimum_passing = 65


class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

pipi = Rules()
pipi.washing_brushes()

class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area
circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    self.diameter = diameter
    print("New circle with diameter: " + str(self.diameter))
teaching_table = Circle(36)

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return ("Circle with radius {r}".format(r=self.radius))
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for item in can_we_count_it:
  if hasattr(item, "count"):
    print(str(type(item)) + "has the count attribute!")
  else:
    print(str(type(item)) + " does not have the count attribute :(")


# Attributes
print(dir(5))
def this_function_is_an_object(weewoo):
  return "Hey"
print(dir(this_function_is_an_object))


class Student:
  
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_average(self):
    sum = 0
    for item in self.grades:
      sum += item.score
    average = sum / (len(self.grades))
    return average


class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self, score):
    self.score = score
    if score >= self.minimum_passing:
      return "Pass"
    else:
      return "Fail"


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(90))
pieter.add_grade(Grade(74))
pieter.add_grade(Grade(90))
pieter.add_grade(Grade(77))
average = pieter.get_average()
print(average)
print(Grade.is_passing())

