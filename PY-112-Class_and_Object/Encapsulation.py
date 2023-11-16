"""
Python does not have the private keyword, unlike some other object oriented languages, but encapsulation can be done.

Instead, it relies on the convention: a class variable that should not directly be accessed should be prefixed with an underscore.

"""


class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
print(obj.__c)



"""
**A single underscore:** Private variable, it should not be accessed directly. But nothing stops you from doing that (except convention).

**A double underscore:** Private variable, harder to access but still possible.

**Both are still accessible:** Python has private variables by convention.

"""

class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version

obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)
