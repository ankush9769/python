class A:
    age=18
    print(age)
    def fun(self,name,age,address):
        print(name," ",age," ",address)
obj=A()
print(A.age)
print(obj.age)
obj.fun("ankush",18,"kandivali")
obj.fun("rishabh",21,"borivali")
obj.fun("rohit",17,"malad")









class A:
    def __init__(self,name,age,address):
        print(name," ",age," ",address)
        
obj=A("ankush",18,"kandivali")
obj2=A("rishabh",21,"malad")









class sports:
    def __init__(self,name,popular, region):
        self.name=name
        self.popular=popular
        self.region=region
    def fun(self):
        print(self.name,"sport","popularity",self.popular,"in",self.region)
obj=sports("foodball","is very high","western")
obj2=sports("cricket","is very high","north")
obj.fun()
obj2.fun()









class student:
    def __init__(self,student_id,student_name,class_name):
        print("studentID:",student_id,",name:",student_name,",the class of the student is",class_name)
obj=student(1001,"ankush","fybsc(cs)")









#create a child class in parent class
class vahical:
    def __init__(self,name,max_speed,mileag):
        self.name=name
        self.max_speed=max_speed
        self.mileag=mileag
class car(vahical):
    pass

obj=car("fortuner",200,18)
print("the name of vahical:",obj.name,",max speed is:",obj.max_speed,",the mileag is:",obj.mileag)



























