# class Grandparent:
#    height = 170
#   satiety = 100
#    age = 60
#
# class Parent(Grandparent)
#    age = 35
#
# class Child(Parent):
#    height = 180
#    age = 15
#    def __init__(self):
#        print(self.height)
#        print(self.age)
#        print(self.satiety)
#
# ch = Child()

# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# class Hi(Hello_world):
#         def hi_printer(self):
#             print(self.hello)
#             print(self._hello)
#             print(self.__hello)
#             print(self.world)
#             print(self._world)
#             print(self.__world)
#
# hello = Hello_world()
# hello.printer()
#
# hi = Hi()
# hi.hi_printer()

class Computer:
   def __init__(self):
      super().__init__()
      self.memory = 128

class Monitor:
   def init__(self):
      super().__init__()
      self.resolution = "4K"
class SmartPhone(Computer, Monitor):
   def print_info(self):
      print(self.memory)
      print(self.resolution)

iphone = SmartPhone()
iphone.print_info()