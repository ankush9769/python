class sports:
    def natureofsports(self):
        print("it is good for helth")
    def popularity(self):
        print("its popularity is high")
class cricket(sports):
    def region(self):
        print("in mumbai")
class football(sports):
    def region(self):
        print("in delhi")
obj1=cricket()
obj2=football()
obj1.natureofsports()
obj1.popularity()
obj1.region()
obj2.region()
