import nath
class Circle:
  def _unit_(self, radius: float):
    if radius <= 0:
      raise ValueError("Радиус должен быть положительным")
    self.radius = radius
  def area(self) > float:
    return math.pi * (self.radius ** 2)
#Implement Circle class
