currect_password="ankushpal"
attempt=0
while (attempt<3):
    password1=input("enter the password=")
    password=password1.lower()
    attempt += 1
    if password==currect_password:
        print("unlock")
        break
    elif password != currect_password and attempt==3:
        print("time up")
        break
    
           
        
