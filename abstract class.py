#abstract class demo

from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def meth(self):
        pass
class laptop(computer):
    def meth(self):
      print("working")

#c=computer()
#c.meth()
lap=laptop()
lap.meth()
