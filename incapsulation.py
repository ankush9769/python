class sports:
    def __init__(self,name,popularity,region):
        self.name=name
        self.popularity=popularity
        self.region=region
    def fun(self):
        print(self.name,"sports","popularity is"+self.popularity,"in "+self.region)
obj1=sports("cricket"," very high","mumbai")
obj1.fun()
        

        
