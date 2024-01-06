class tour:
    def __init__(self,noofadults,noofkids,kilometers,totfare):
        self.noofadults=noofadults
        self.noofkids=noofkids
        self.kilometers=kilometers
        self.totfare=totfare
    def fare(self):
        if self.kilometers>=1000:
            print("the fare for adults=",500*self.noofadults)
            print("the fare for kids=",250*self.noofkids)
            print("totfare for tour=",500*self.noofadults+250*self.noofkids) 
            print()
        elif self.kilometers<1000 and self.kilometers>=500:
            print("the fare for adults=",300*self.noofadults)
            print("the fare for kids=",150*self.noofkids)
            print("totfare for tour=",300*self.noofadults+150*self.noofkids)
            print()
        elif self.kilometers<500:
            print("the fare for adults=",200*self.noofadults)
            print("the fare for kids=",100*self.noofkids)
            print("totfare for tour=",200*self.noofadults+100*self.noofkids)
            print()
        else:
            print("invalid input")
          
            
obj1=tour(2,3,850,"00")
obj1.fare()

            
