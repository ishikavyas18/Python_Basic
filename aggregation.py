# aggregation

class Country:
    def __init__(self,name=None,population=0):
        self.name=name
        self.population=population

    def pirint(self):
        print("name is :",self.name)
        print("population is :",self.population)
class person(Country):
    def __init__(self,name,country):
        self.name=name
        self.country=country

    def pirint(self):
        print("name of person is :",self.name)
        self.country.pirint()

count=Country("us",2425)
p=person("hussainm",count)
p.pirint()
# to delete object use del
del p
print("")
count.pirint()
