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