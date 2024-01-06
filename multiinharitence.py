class worldcupcricket:
    def strategy(self):
        print("all teams have defined a winning strategy")
class noofteams(worldcupcricket):
    def compete(self):
        print("every team is competing with other team")
class cricket(noofteams):
    def mission(self):
        print("mission is completed")
obj1=cricket()
obj1.strategy()
obj1.compete()
obj1.mission()
